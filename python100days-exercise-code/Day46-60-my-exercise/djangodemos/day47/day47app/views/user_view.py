from day47app.models import UserInfo
from django.shortcuts import render,redirect

def user_list(req):
    users = UserInfo.objects.all()
    
    return render(req,'user_list.html',{'users':users})