from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_view'),
    path('logout/', views.logout, name='lgout_view'),
]
