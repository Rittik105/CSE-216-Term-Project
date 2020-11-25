from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    if request.session.has_key('admin_name'):
        return render(request, "home_admin/home_admin.html")
    return redirect('not_lgin_view')

def logout(request):
    if request.session.has_key('admin_name'):
        request.session.pop('admin_name')
        return redirect("login_view")
    return render(request, "admin_login/admin_login.html", context = {'status':'Log in First'})
