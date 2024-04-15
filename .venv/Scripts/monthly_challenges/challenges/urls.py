from django.urls import path,include
from . import views

urlpatterns = [
    path('January', views.index)
]