from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import ConsumptionForm, MacroGoalsForm
from .models import UserConsumption, CalorieGoal, MacroGoal
from django.db.models import Sum
from datetime import datetime
from django.views import View
from django.http import JsonResponse
from calendar import HTMLCalendar


def chart(request):
    labels = ["Calories", "Input"]
    remainder = "20"
    data = ["80", remainder]

       # queryset = City.objects.order_by('-population')[:5]
        #for city in queryset:
           # labels.append(city.name)
           # data.append(city.population)

    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })


class UpdateMacrosView(View):
    def get(self, request):
        return redirect('/')

    def post(self, request):
        # Store submitted data from user into form variable
        form = MacroGoalsForm(request.POST)
        if form.is_valid():
            # Get current user
            current_user = request.user
            # Retrieving previous goal data from current user in the MacroGoal database
            previous = MacroGoal.objects.filter(user=current_user)
            # Deleting that data (later to be changed to just the current day)
            previous.delete()

            # Assign data from form into variables
            fat = form.cleaned_data['daily_fat']
            protein = form.cleaned_data['daily_protein']
            carbohydrates = form.cleaned_data['daily_carbohydrates']
            # Pile data into variable to be saved to database
            new_macros = MacroGoal(user=current_user, daily_fat = fat, daily_protein= protein,
                                    daily_carbohydrates= carbohydrates)
            # Save Data
            new_macros.save()
            # Redirect to homepage
            return redirect('/')
        else:
            messages.info(request, "Invalid Entry")
            return redirect('/')


def delete(request, d):
    UserConsumption.objects.filter(id=d).delete()
    return redirect('/')


def goal(request):
    if request.method == "POST":
        goal = request.POST["total"]
        if len(goal) > 0:
            current_user = request.user
            delete = CalorieGoal.objects.filter(user=current_user)
            delete.delete()
            day = CalorieGoal(user=current_user, daily_calories=goal)
            day.save()
            print("Saved to database")
            return redirect('/')
        else:
            messages.info(request, "Invalid Entry")
            return redirect("/")
    else:
        return redirect('register')


def main(request):
    if request.method == 'POST':
        form = ConsumptionForm(request.POST)
        if form.is_valid():
            user = request.user
            food = form.cleaned_data['food']
            calories = form.cleaned_data['calories']
            fat = form.cleaned_data['fat']
            protein = form.cleaned_data['protein']
            carbohydrates = form.cleaned_data['carbohydrates']
            datestamp = datetime.today().strftime('%Y-%m-%d')
            print(datestamp)

            data = UserConsumption(user=user, food=food, calories=calories, fat=fat, protein=protein,
                                   carbohydrates=carbohydrates, datestamp=datestamp)
            data.save()
            return redirect('/')
        else:
            print("Invalid Form")
            return redirect('register')

    else:
        form = ConsumptionForm()
        macro_form = MacroGoalsForm()
        username = None
        if request.user.is_authenticated:
            current_user = request.user

            # Aggregate meals ate today to return daily calorie intake and macro nutrition
            user = UserConsumption.objects.filter(user=current_user, datestamp=datetime.today().strftime('%Y-%m-%d'))
            calories = user.aggregate(Sum('calories')).get('calories__sum')
            fat = user.aggregate(Sum('fat')).get('fat__sum')
            carbohydrates = user.aggregate(Sum('carbohydrates')).get('carbohydrates__sum')
            protein = user.aggregate(Sum('protein')).get('protein__sum')

            daily_total = {'calories': calories,
                           'fat': fat,
                           'carbohydrates': carbohydrates,
                           'protein': protein,
                           }
            daily = UserConsumption.objects.all().filter(user=current_user,
                                                         datestamp=datetime.today().strftime('%Y-%m-%d'))

            # Calculate calories remaining from comsumed
            user_goal = CalorieGoal.objects.filter(user=current_user)
            goal = user_goal.aggregate(Sum('daily_calories')).get('daily_calories__sum')
            if calories is not None:
                if calories > goal:
                    remainder = 0
                else:
                    remainder = goal - calories
            else:
                calories, remainder, fat, carbohydrates, protein = 0, 0, 0 , 0, 0


            # Calculates Calorie %
            percentage = int((calories / goal) * 100)

            # Get Nutrition Goals
            target = MacroGoal.objects.filter(user=current_user).last()
            fat_target = int(target.daily_fat)
            protein_target = int(target.daily_protein)
            carbs_target = int(target.daily_carbohydrates)
            if fat_target > 1:
                print(fat_target - fat)
                # Calculate Macro Goal %
                fat_percent = int((fat / fat_target * 100))
                protein_percent = int((protein / protein_target * 100))
                carbs_percent = int((carbohydrates / carbs_target * 100))
                print(fat_percent, protein_percent, carbs_percent)
            else:
                fat_percent, carbs_percent, protein_percent = 0,0,0

            # chart info
            chart_labels = ["CC", "CR"]
            chart_remainder = 100 - percentage
            chart_data = [percentage, chart_remainder]
            # Store all variable in root
            root = {
                'chart_labels': chart_labels,
                'chart_data': chart_data,
                'fat_target' : fat_target,
                'protein_target': protein_target,
                'carbs_target': carbs_target,
                'fat_percent': fat_percent,
                'protein_percent': protein_percent,
                'carbs_percent': carbs_percent,
                'daily': daily,
                'daily_total': daily_total,
                'calories': calories,
                'fat': fat,
                'carbohydrates': carbohydrates,
                'protein': protein,
                'percentage': percentage,
                'remainder': remainder
                 }

            return render(request, 'main.html', {'form': form, 'macro': macro_form, 'root': root})

        else:
            pass
        return render(request, 'main.html', {'form': form, 'macro': macro_form})


def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print(f"User {user} has logged in.")
            return redirect('/')
        else:
            messages.info(request, "Invalid Username or Password.")
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                                username=username, password=password1)
                user.save()
                print('User Created')
                return redirect('login')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('register')
    else:
        return render(request, 'register.html')