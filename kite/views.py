from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from kite.models import userData, product
from . import Templates


# Create your views here.
def index(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def home(request):
    products = product.objects.all()
    param = {'product': products}
    return render(request, 'homepage.html', param)

def authen(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request)
        return redirect('/home')
    else:
        return HttpResponse("Wrong credentials")

def check(request):
    fname = request.POST.get('first_name', '')
    lname = request.POST.get('last_name', '')
    username = request.POST.get('username', '')
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    confirm = request.POST.get('confirm_password', '')
    if User.objects.filter(username = username).exists():
        return HttpResponse("User already exists")
    if len(password) < 5:
        return HttpResponse("Passwords should be greater than 5")
    elif password != confirm:
        return HttpResponse("passwords does not match")
    else:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name=fname
        user.last_name=lname
        user.save()
        return HttpResponse("User created")