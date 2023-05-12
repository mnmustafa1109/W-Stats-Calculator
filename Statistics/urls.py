# pages/urls.py
from django.urls import path

from .views import take_input, display_result

urlpatterns = [
    path("", take_input, name="home"),
    path("result", display_result, name="result")
]