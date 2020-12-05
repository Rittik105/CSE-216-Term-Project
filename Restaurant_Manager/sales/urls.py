from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_order_list, name='order_list'),
]
