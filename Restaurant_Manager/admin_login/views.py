from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.


#this function handles the login part
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


#shows home page
def home(request):
    if request.session.has_key('admin_name'):
        return render(request, "admin_login/home_admin.html")
    return redirect('not_lgin_view')


#this function generates the table in managers showing all the managers signed up in the system
def table(request):
    if request.session.has_key('admin_name'):
        if request.method == "GET":
            cursor = connection.cursor()
            sql = "SELECT NAME, MANAGER_ID, EMAIL, PHONE_NUM FROM MANAGER ORDER BY MANAGER_ID"
            cursor.execute(sql)
            result = cursor.fetchall()
            connection.close()
            dict = []

            for r in result:
                name = r[0]
                MANAGER_ID = r[1]
                email = r[2]
                phone = r[3]
                row = {'name':name, 'id':MANAGER_ID, 'mail':email, 'num':phone}
                dict.append(row)

            return render(request, 'admin_login/managers.html', context = {'dict':dict})
    return redirect('not_lgin_view')


#adds new manager to the database that can be used to log into the admin panel
def signup(request):
    if request.session.has_key('admin_name'):
        if request.method == "POST":
            name = request.POST.get('name')
            mail = request.POST.get('mail')
            print(request.POST.get('pass'))
            password = make_password( request.POST.get('pass') )
            address = request.POST.get('address')
            phone = request.POST.get('phone')

            cursor = connection.cursor()
            sql = 'SELECT MAX(MANAGER_ID) FROM MANAGER'
            cursor.execute(sql)
            last_id = cursor.fetchone()
            last_id = last_id[0]
            if last_id is not  None:
                user_id = last_id + 1
            else:
                user_id = 1

            cursor = connection.cursor()
            sql = "INSERT INTO MANAGER VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, [user_id, name, mail, phone, password, address])

            return render(request, "admin_login/success.html")

        return render(request, 'admin_login/signup.html')

    return redirect('not_lgin_view')


#if not logged in this funcrion is called from anywhere where log in is required to view content
def not_lgin(request):
    return render(request, "admin_login/not_loggedin.html")


#logs user out of the session
def logout(request):
    if request.session.has_key('admin_name'):
        request.session.pop('admin_name')
        return redirect("login_view")
    return render(request, "admin_login/admin_login.html", context = {'status':'Log in First'})
#if request.session.has_key('admin_name'):
#return redirect('not_lgin_view')
