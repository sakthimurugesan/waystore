from django.contrib import messages
from django.shortcuts import render, redirect
from account.forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout as lo


def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "User created")
            return redirect("login_page")

    return render(request, "account/page-user-register.html", {"form": form, })


def login_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            request.session['email']=email
            request.session.save()

            messages.success(request, message='Login Successful')
            return redirect("index")
        else:

            return redirect("login_page")


    return render(request, "account/page-user-login.html")


def add_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created")
            return redirect("login_page")
    return redirect("register")

def logout(request):
    if request.user.is_authenticated:
        lo(request)
        messages.success(request, "Logged Out")
    return redirect("index")