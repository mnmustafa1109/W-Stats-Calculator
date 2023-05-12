# pages/urls.py
from django.urls import path

from .views import take_input

urlpatterns = [
    path("", take_input, name="home"),
]