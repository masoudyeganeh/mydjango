from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posts, name="all-posts"),
    path('<int:pid>', views.post, name="posturl")
]