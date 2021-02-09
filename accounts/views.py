from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User


def login(request):
    context = {
        'title': "Login"
    }
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        if user_name == "":
            messages.error(request, "Username is required")
            return redirect('login')
        if password == "":
            messages.error("Password is required")
            return redirect("login")
        user = auth.authenticate(username=user_name, password=password)
        if user is not None:
            auth.login(request=request, user=user)
            messages.success(request, "logged in successfully")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login')
    return render(request, "accounts/login.html", context)


def register(request):
    context = {
        'title': "Register"
    }
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        user_name = request.POST.get('userName')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        if first_name == '':
            messages.error(request, 'First Name is Required')
            return redirect('register')

        if last_name == '':
            messages.error(request, "Last Name is required")
            return redirect('register')

        if email == '':
            messages.error(request, 'Email is requried')
            return redirect('register')

        if user_name == '':
            messages.error(request, 'UserName is required')
            return redirect('register')

        if password == '':
            messages.error(request, 'Password is required')
            return redirect('register')

        if password == password_confirm:
            user = User.objects.filter(email=email).exists()
            if user:
                messages.error(request, "Email already exists")
                return redirect('register')
            user = User.objects.filter(username=user_name).exists()
            if user:
                messages.error(request, "Username already exists")
                return redirect("register")
            user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                            email=email, password=password, username=user_name)
            user.save()
            messages.success(
                request, "Successfully Registered")
            return redirect("login")
        else:
            messages.error(request, 'Password is required')
            return redirect('register')
    else:
        return render(request, "accounts/register.html", context)


def dashboard(request):
    context = {
        'title': "Dashboard"
    }
    return render(request, "accounts/dashboard.html", context)


def logout(request):
    auth.logout(request)
    messages.success(message="logged out", request=request)
    return redirect('index')
