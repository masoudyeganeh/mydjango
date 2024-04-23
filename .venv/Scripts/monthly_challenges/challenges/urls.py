from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('<str:month>', views.monthly_challenge),
    path('<int:month>', views.monthly_challenge_by_number, name="month-challenge")
]