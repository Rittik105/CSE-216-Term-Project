from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "customer_login/login.html")
