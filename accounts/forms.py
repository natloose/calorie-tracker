from django import forms
from .models import UserConsumption, MacroGoal


class ConsumptionForm(forms.ModelForm):
    class Meta:
        model = UserConsumption
        fields = [
            'food',
            'calories',
            'fat',
            'protein',
            'carbohydrates',
        ]
        widgets = {
            'food': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Food Name'}),
            'calories': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Total Calories'}),
            'fat': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Fat(g)'}),
            'protein': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Protein(g)'}),
            'carbohydrates': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Carbs(g)'}),
        }


class MacroGoalsForm(forms.ModelForm):
    class Meta:
        model = MacroGoal
        fields = [
            'daily_fat',
            'daily_protein',
            'daily_carbohydrates'
        ]

        widgets = {
            'daily_fat': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '(g)'}),
            'daily_protein': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '(g)'}),
            'daily_carbohydrates': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '(g)'}),
        }