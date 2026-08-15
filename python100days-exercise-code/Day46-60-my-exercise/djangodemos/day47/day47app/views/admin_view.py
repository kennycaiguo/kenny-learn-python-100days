from django.http import HttpResponse
from django.shortcuts import redirect, render

from day47.forms.day47forms import AdminAddForm, AdminEidtForm
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
    page_obj = Pagination(req,admins,page_size=3)
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
    title = "编辑管理员"
    admin = Admin.objects.filter(id=nid).first()
    # handle get method
    if req.method == "GET":
        form = AdminEidtForm(instance=admin)
        return render(req,"admin_add_edit.html",{"form":form,"title":title})
    # handle post
    form = AdminEidtForm(data=req.POST,instance=admin)
    if form.is_valid():
        form.save(commit=True)
        return redirect("/admin/list/")
    return render(req,"admin_add_edit.html",{"form":form,"title":title})


def admin_del(req,nid):
    Admin.objects.filter(id=nid).delete()
    return redirect('/admin/list/')
