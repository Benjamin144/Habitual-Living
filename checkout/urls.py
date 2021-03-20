from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, names='checkout')
]