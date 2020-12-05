from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from django.http import JsonResponse
import json

# Create your views here.
def store(request):
    if request.session.has_key('customer_name'):
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
    return redirect('nlview')


def cart(request):
    if request.session.has_key('customer_name'):
        customer = request.session.get('customer_name')
        data = json.loads(request.data)
        product = data['productId']
        console.log(customer)
    context = {}
    return render(request,'store/cart.html')

def updateItem(request):
    return JsonResponse('Item was added')

def not_lgin(request):
    return render(request, "store/ntlgin.html")
