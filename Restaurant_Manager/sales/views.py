from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from datetime import date
# Create your views here.


def show_order_list(request):
    if request.session.has_key('admin_name'):
        from_date = date.today().strftime("%Y-%m-%d")
        to_date = date.today().strftime("%Y-%m-%d")
        order_type = "All"


        if request.method == "POST":
            if request.POST.get("from_date"):
                from_date = str(request.POST.get("from_date"))
            if request.POST.get("to_date"):
                to_date = str(request.POST.get("to_date"))
            order_type = request.POST.get("type")

        dict = []
        total_sale = 0

        if order_type == "All" or order_type == "Dine-In Orders":
            cursor = connection.cursor()
            sql = "SELECT DATE_TIME, ORDER_ID, TABLE_NO, M.NAME, E.NAME, TOTAL_BILL FROM OFF_ORDER O JOIN MANAGER M ON (M.MANAGER_ID = O.MANAGER_ID) JOIN EMPLOYEES E ON (E.EMPLOYEE_ID = O.EMPLOYEE_ID) WHERE DATE_TIME >= TO_DATE(%s, 'YYYY-MM-DD') AND DATE_TIME <= TO_DATE(%s, 'YYYY-MM-DD')+1 ORDER BY DATE_TIME"
            cursor.execute(sql, [from_date, to_date])
            result = cursor.fetchall()
            connection.close()

            for r in result:
                time_stamp = r[0]
                order_id = r[1]
                table = r[2]
                manager = r[3]
                waiter = r[4]
                total = r[5]
                total_sale = total_sale + float(total)
                row = {'time_stamp':time_stamp, 'order_id':order_id, 'table':table, 'manager':manager, 'waiter':waiter, 'total':total}
                dict.append(row)

        if order_type == "All" or order_type == "Home Delivery Orders":
            cursor = connection.cursor()
            sql = "SELECT DATE_TIME, ORDER_ID, CUSTOMER_ID, TOTAL_BILL FROM ON_ORDER WHERE DATE_TIME >= TO_DATE(%s, 'YYYY-MM-DD') AND DATE_TIME <= TO_DATE(%s, 'YYYY-MM-DD')+1 AND STATUS = 'ACCEPTED' ORDER BY DATE_TIME "
            cursor.execute(sql, [from_date, to_date])
            result = cursor.fetchall()
            connection.close()

            for r in result:
                time_stamp = r[0]
                order_id = r[1]
                table = r[2]
                manager = "N/A"
                waiter = "N/A"
                total = r[3]
                total_sale = total_sale + float(total)
                row = {'time_stamp':time_stamp, 'order_id':order_id, 'table':table, 'manager':manager, 'waiter':waiter, 'total':total}
                dict.append(row)

        return render(request, "sales/sales_table.html", context={'dict':dict, 'from':from_date, 'to':to_date, "total_sale":total_sale, 'type':order_type})
    return redirect('not_lgin_view')
