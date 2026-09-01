from bson import is_valid
from django.http import HttpResponse
from django.shortcuts import redirect, render

from day47app.utils.day47forms import AdminAddForm, AdminEditForm, AdminResetForm
from day47app.models import Admin
from day47app.utils.pagination import Pagination
from django.shortcuts import render


def admin_list(req):
    # search ability
    term = {}
    kw = req.GET.get("kw","")
    if kw:
        term["username__contains"] = kw

    admins = Admin.objects.filter(**term)
    # print(admins)
    page_obj = Pagination(req,admins,page_size=6)
    page_queryset = page_obj.page_queryset
    page_str = page_obj.gen_html()
    return render(req,"admin_list.html",{"admins":page_queryset,"page_str":page_str})

def admin_add(req):
    # handle get
    title = "新增管理员"
    if req.method == "GET":
        form = AdminAddForm()
        return render(req,"admin_add_edit.html",{"form":form,"title":title})
    # handle post
    # get the post data and do the verify
    form = AdminAddForm(data=req.POST)
    if form.is_valid():
        form.save(commit=True)
        return redirect("/admin/list/")
    return render(req,"admin_add_edit.html",{"form":form,"title":title})


def admin_edit(req,nid):
    # 先确保传递过来的id有效,如果不是一个有效的id，就转到管理员列表让他写在一个管理员
    row = Admin.objects.filter(id=nid)
    if not row:
        # return redirect("/admin/list/") #方式1，重定向
        # return render(req,"error.html")  #方式2，渲染一个错误页面
        return render(req,"error2.html",{"msg":f"没有id为{nid}的管理员"})  #方式2，渲染一个错误页面
    title = "编辑管理员"
    admin = Admin.objects.filter(id=nid).first()
    # handle get method
    if req.method == "GET":
        form = AdminEditForm(instance=admin)
        return render(req,"admin_add_edit.html",{"form":form,"title":title})
    # handle post
    form = AdminEditForm(data=req.POST,instance=admin)
    if form.is_valid():
        form.save(commit=True)
        return redirect("/admin/list/")
    return render(req,"admin_add_edit.html",{"form":form,"title":title})


def admin_del(req,nid):
    row = Admin.objects.filter(id=nid)
    if not row:
        return redirect("/admin/list/")
    row.delete()
    return redirect('/admin/list/')

def admin_reset(req,nid):
    row = Admin.objects.filter(id=nid)
    if not row:
        return render(req,"error2.html",{"msg":f"没有id为{nid}的管理员"})
    admin = row.first()
    if req.method == 'GET':
        form = AdminResetForm()
        return render(req,'admin_add_edit.html',{"form":form,"title":f"重置管理员：{admin.username}的密码"})
    form = AdminResetForm(data=req.POST,instance=admin)
    if form.is_valid(): #数据校验成功
        form.save(commit=True)
        return redirect("/admin/list/")
    # 数据校验失败，就显示错误并且停留在本页面
    return render(req,'admin_add_edit.html',{"form":form,"title":f"重置管理员：{admin.username}的密码"})