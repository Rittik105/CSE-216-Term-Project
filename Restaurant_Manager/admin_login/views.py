from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

def login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        cursor = connection.cursor()
        sql = "SELECT NAME, PASSWORD FROM MANAGER WHERE EMAIL = %s"
        cursor.execute(sql, [email])
        result = cursor.fetchone()
        connection.close()

        if result and check_password(password, result[1]):
            admin_name = result[0]
            request.session['admin_name'] = admin_name
            return redirect('home_view')
        else:
            return render(request, "admin_login/admin_login.html", context = {'status':'Log in failed'})


    return render(request, "admin_login/admin_login.html")
