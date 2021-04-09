
from django.contrib import admin
from django.urls import path

from bloodbank import views

urlpatterns = [
    path('',views.index,name="index"),
    path('stock/',views.stock,name="stock"),
    path('collect/',views.collect,name="collect"),
    path('give/',views.give,name="give"),
]