from django.shortcuts import redirect, render


def login(request):
    context = {
        'title': "Login"
    }
    return render(request, "accounts/login.html", context)


def register(request):
    context = {
        'title': "Register"
    }
    return render(request, "accounts/register.html", context)


def dashboard(request):
    context = {
        'title': "Dashboard"
    }
    return render(request, "accounts/dashboard.html", context)


def logout(request):
    return redirect('index')
