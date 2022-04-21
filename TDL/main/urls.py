from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path ('customer/<str:pk>/', views.customer, name="customer"),
    path ('delete_item/<str:pk>/', views.delete, name="delete"),
    path ('finished/<str:pk>/', views.finished, name="finish"),
    path('register/', views.register, name="register"),
]