from django.urls import path
from authApp import views

urlpatterns = [
    path("", views.login, name="login"),
]