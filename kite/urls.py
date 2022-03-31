from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login, name='login'),
    path('check', views.check, name='check'),
    path('authen', views.authen, name='authen'),
    path('home', views.home, name='home'),
]
