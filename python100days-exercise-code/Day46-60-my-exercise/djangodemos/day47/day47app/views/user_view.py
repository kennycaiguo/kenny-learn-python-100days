from django import forms

from day47app.models import UserInfo,Department
from django.shortcuts import render,redirect
from django.http import HttpResponse

def user_list(req):
    users = UserInfo.objects.all()
    
    return render(req,'user_list.html',{'users':users})


class MyForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['name','password','age','account','create_time','gender','dep']


def user_add(req):
    if req.method == 'GET':
        form = MyForm()
        return render(req,'user_add.html',{'form':form})
    # method post
    name = req.POST.get('name')
    pwd =  req.POST.get('pwd')
    age =  req.POST.get('age')
    acc =  req.POST.get('acc')
    ctime =req.POST.get('ctime')
    gender=req.POST.get('gender')
    dep =  req.POST.get('dep')
    UserInfo.objects.create(name=name,password=pwd,age=age,account=acc,create_time=ctime,gender=gender,dep_id=dep)
    return redirect("/user/list")