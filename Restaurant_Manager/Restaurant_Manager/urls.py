"""Restaurant_Manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
<<<<<<< HEAD
=======
    path('', include('customer_login.urls'), name="customers"),
    path('store/', include('store.urls'), name="store"),
    path('home/', include('customer_home.urls'), name="home"),
>>>>>>> 06c8af6afb082f9dde5dd4f474fa79e945f1240d
    path('admin/', include('admin_login.urls'), name="alogin"),
    path('menu/', include('menu.urls'), name="menu"),
    path('order/', include('admin_order.urls'), name="order"),
    path('sale/', include('sales.urls'), name="sale"),
]
