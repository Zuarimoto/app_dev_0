"""
URL configuration for ninja_turts project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/name")
def name(request):
    return {"name": "Zura"}

@api.get("/add")
def add(request, a:int, b:int):
    return {"result": a+b}

@api.get("/subtraction")
def subtract(request, a:int, b:int):
    return{"result": a-b}

@api.get("multiplication")
def multiply(request, a:int, b:int):
    return{"result": a*b}

@api.get("division")
def divide(request, a:int, b:int):
    return{"result": a/b}

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",api.urls)
]
