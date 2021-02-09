"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import HttpResponse, render
from django.conf import settings
from django.conf.urls.static import static


def response(func):
    def returnResponse(request):
        func(request)
        if request.method == 'GET':
            context = {
                "title": "Homepage"
            }
            my_name = request.GET.get("my_name")
            if my_name:
                context['my_name'] = my_name
            return render(request, "pages/home/index.html", context)
        elif request.method == 'POST':
            name = request.POST.get("name")
            return HttpResponse(f"Name is {name}")
    return returnResponse


@response
def makeResponse(request):
    print(request)


def index(request):
    return makeResponse(request)


def about(request):
    return HttpResponse("<h1>About Page</h1>")


urlpatterns = [
    path("", include("pages.urls")),
    path("listings/", include("listings.urls")),
    path("aboutPage", about),
    path("realtors/", include("realtors.urls")),
    path("auth/", include("accounts.urls")),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
