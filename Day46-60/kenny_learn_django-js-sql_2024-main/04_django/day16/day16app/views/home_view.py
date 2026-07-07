from django.http import HttpResponse
from django.shortcuts import render, redirect
from day16app import models  # 导入models因为以后可能里面会有很多类不能一个一个导入
from day16app.utils.pagination import Pagination
from day16app.form import day16forms


# Create your views here.

def home(req):
    return render(req, "home.html")


def index(req):
    return render(req, "home.html")