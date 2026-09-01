from ast import If

from django import forms



from day47app.models import UserInfo,Department
from django.shortcuts import render,redirect
from django.http import HttpResponse

from day47app.utils.day47forms import UserInfoForm
from day47app.utils.pagination import Pagination

def user_list(req):
    users = UserInfo.objects.all()
    # 分页
    # 1.实例化分页类的对象
    page_obj = Pagination(req,users,page_size=3)
    # 2.获取分页数据
    page_queryset = page_obj.page_queryset
    # 3.获取分页器的html字符串
    page_str = page_obj.gen_html()
    return render(req,'user_list.html',{'users':page_queryset,"page_str":page_str})

def user_add(req):
    if req.method == 'GET':
        form = UserInfoForm()
        return render(req,'user_add.html',{'form':form})
    # method post
    form = UserInfoForm(req.POST)
    # VERIFY
    if form.is_valid():
        form.save(commit=True)
        return redirect("/user/list")
    return render(req,'user_add.html',{'form':form})  

def user_edit(req,nid):
    # 先判断用户传递过来的nid是否有效，如果是无效的，重定向到用户列表
    row = UserInfo.objects.filter(id=nid)
    if not row:
        return redirect("/user/list/")
    # get method handling
    user = UserInfo.objects.filter(id=nid).first()
    print(user.password)
    if req.method == "GET":
        form = UserInfoForm(instance=user)
        return render(req,"user_edit.html",{"form":form})
    # post method data handling
    # print(req.POST)
    form = UserInfoForm(instance=user,data=req.POST)
    if form.is_valid():
        form.save()
        return redirect("/user/list/")   
    return render(req,"user_edit.html",{"form":form})

def user_del(req):
    nid = req.GET.get('nid')
    # print(nid)
    user = UserInfo.objects.filter(id=nid)
    if not user:
        return redirect("/user/list") # 如果id无效，我们就转到用户列表
    user.delete()
    return redirect('/user/list/')