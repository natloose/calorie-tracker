from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('', views.main, name="forms"),
    path('delete/<str:d>/', views.delete, name="delete"),
    path('goal', views.goal, name="goal"),
    path('macros', views.UpdateMacrosView.as_view(), name="macros"),
    path('chart', views.chart, name='chart'),
]
