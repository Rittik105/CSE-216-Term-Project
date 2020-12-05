from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from .utils import generate_primary_key
# Create your views here.

def place_order(request):
    if request.session.has_key('admin_name'):
        cursor = connection.cursor()
        sql = "SELECT FOOD_ID, NAME, PRICE, DESCRIPTION, PICTURE FROM FOOD ORDER BY FOOD_ID"
        cursor.execute(sql)
        result = cursor.fetchall()
        connection.close()
        dict = []
        for r in result:
            food_id = r[0]
            item_name = r[1]
            price = r[2]
            description = r[3]
            picture = r[4]
            row = {'id':food_id, 'name':item_name, 'price':price, 'desc':description, 'pic':picture}
            dict.append(row)

        cursor = connection.cursor()
        sql = "SELECT NAME, EMPLOYEE_ID FROM EMPLOYEES WHERE JOB_ID = (SELECT JOB_ID FROM JOB_TYPE WHERE JOB_NAME = 'WAITER')"
        cursor.execute(sql)
        result = cursor.fetchall()
        connection.close()
        dict2 = []
        for r in result:
            name = r[0]
            id = r[1]
            row = {'name':name, 'id':id}
            dict2.append(row)

        if request.method == "POST":
            cursor = connection.cursor()
            sql = 'SELECT MAX(ORDER_ID) FROM OFF_ORDER'
            cursor.execute(sql)
            order_id = cursor.fetchone()[0]
            if order_id is not None:
                order_id = int(order_id.split(sep="_")[0])
            order_id = generate_primary_key(order_id)
            order_id = 'OFF_' + str(order_id)

            sql = "SELECT MAX(FOOD_ID) FROM FOOD"
            cursor.execute(sql)
            total_item = cursor.fetchone()[0]

            for i in range(1, total_item+1):
                if int(request.POST.get(str(i))) > 0:
                    cursor = connection.cursor()
                    sql = 'SELECT MAX(ITEM_ID) FROM ORDERED_ITEMS'
                    cursor.execute(sql)
                    item_id = cursor.fetchone()
                    item_id = item_id[0]
                    item_id = generate_primary_key(item_id)
                    sql = "INSERT INTO ORDERED_ITEMS VALUES (%s, %s, %s, %s)"
                    cursor.execute(sql, [item_id, order_id, i, int(request.POST.get(str(i)))])

            table_no = request.POST.get('table')

            cursor = connection.cursor()
            total_bill = cursor.callfunc('TOTAL_BILL', float, [order_id])

            cursor = connection.cursor()
            sql = 'SELECT MANAGER_ID FROM MANAGER WHERE NAME = %s'
            cursor.execute(sql, [request.session.get('admin_name')])
            man_id = cursor.fetchone()[0]

            emp_id = request.POST.get('waiter')

            cursor = connection.cursor()
            sql = "INSERT INTO OFF_ORDER VALUES (%s, %s, %s, SYSDATE,%s, %s)"
            cursor.execute(sql, [order_id, table_no, total_bill, man_id, emp_id])


        return render(request, "admin_order/order_page.html", context={'dict':dict, 'dict2':dict2})
    return redirect('not_lgin_view')
