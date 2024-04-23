from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('<str:month>', views.monthly_challenge, name="month-challenge"),
    path('<int:month>', views.monthly_challenge_by_number)
]