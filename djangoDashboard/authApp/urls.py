from django.urls import path
from authApp import views

urlpatterns = [
    path("", views.Signin, name="Signin"),
    path("Signup", views.Signup, name="Signup"),
]