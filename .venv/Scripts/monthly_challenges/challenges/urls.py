from django.urls import path,include
from . import views

urlpatterns = [
    path('<str:month>', views.monthly_challenge)
]