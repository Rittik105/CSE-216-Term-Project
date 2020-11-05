from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def table(request):
    if request.method == "GET":
        cursor = connection.cursor()
        sql = "SELECT NAME, MANAGER_ID, EMAIL, PHONE_NUM, DOB FROM MANAGER"
        cursor.execute(sql)
        result = cursor.fetchall()
        dict = []

        for r in result:
            name = r[0]
            MANAGER_ID = r[1]
            email = r[2]
            phone = r[3]
            dob = r[4]
            row = {'name':name, 'id':MANAGER_ID, 'mail':email, 'num':phone, 'dob':dob}
            dict.append(row)

        return render(request, 'managers/managers.html', context = {'dict':dict})
