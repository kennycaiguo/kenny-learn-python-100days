from day47app.models import UserInfo,Department
from django.shortcuts import render,redirect
from django.http import HttpResponse

def user_list(req):
    users = UserInfo.objects.all()
    
    return render(req,'user_list.html',{'users':users})

def user_add(req):
    if req.method == 'GET':
        context={
            "g_choice":UserInfo.gender_choices,
            "deps":Department.objects.all()
        }
        return render(req,'user_add.html',context)
    return HttpResponse('添加用户成功...')