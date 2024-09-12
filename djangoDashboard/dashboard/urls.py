from django.urls import path, include
from dashboard import views

urlpatterns = [
    path("", views.index, name="dashboard"),
    path("contact", views.contact, name="contact"),
]
