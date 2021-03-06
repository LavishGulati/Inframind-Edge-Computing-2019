from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('billing/<slug:contact>', views.billing, name='billing'),
]
