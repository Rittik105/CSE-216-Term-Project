from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def store(request):
    if request.method == "GET":
        cursor = connection.cursor()
        sql = "SELECT FOOD_ID,NAME, PRICE FROM FOOD ORDER BY FOOD_ID"
        cursor.execute(sql)
        result = cursor.fetchall()
        connection.close()
        dict = []

        for r in result:
            id = r[0]
            name = r[1]
            price = r[2]
            row = {'id':id, 'name':name, 'price':price}
            dict.append(row)

        return render(request, 'store/store.html', context = {'dict':dict})


def cart(request):
    context = {}
    return render(request,'store/cart.html')
