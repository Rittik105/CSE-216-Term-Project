from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
# Create your views here.

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        cursor = connection.cursor()
        sql = 'SELECT PASSWORD FROM MANAGER WHERE NAME = %s'
        cursor.execute(sql, [username])
        result = cursor.fetchone()

        if result and password == result[0]:
            return redirect('home/', 'home')
        else:
            return render(request, "admin_login/admin_login.html", context = {'status':'Log in failed'})


    return render(request, "admin_login/admin_login.html")
