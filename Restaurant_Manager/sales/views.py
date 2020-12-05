from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
# Create your views here.


def show_order_list(request):
    if request.session.has_key('admin_name'):
        cursor = connection.cursor()
        sql = "SELECT DATE_TIME, ORDER_ID, TABLE_NO, M.NAME, E.NAME, TOTAL_BILL FROM OFF_ORDER O JOIN MANAGER M ON (M.MANAGER_ID = O.MANAGER_ID) JOIN EMPLOYEES E ON (E.EMPLOYEE_ID = O.EMPLOYEE_ID) ORDER BY DATE_TIME"
        cursor.execute(sql)
        result = cursor.fetchall()
        connection.close()
        dict = []

        for r in result:
            time_stamp = r[0]
            order_id = r[1]
            table = r[2]
            manager = r[3]
            waiter = r[4]
            total = r[5]
            row = {'time_stamp':time_stamp, 'order_id':order_id, 'table':table, 'manager':manager, 'waiter':waiter, 'total':total}
            dict.append(row)

        return render(request, "sales/sales_table.html", context={'dict':dict})
    return redirect('not_lgin_view')
