from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.table, name='table_view'),
    path('admin_signup/', views.signup, name='form_view'),
    path('not_lgin/', views.not_lgin, name='not_lgin_view'),
]
