from django.http import HttpResponse
from django.shortcuts import render, redirect
from day16app import models  # 导入models因为以后可能里面会有很多类不能一个一个导入
from day16app.utils.pagination import Pagination
from day16app.form import day16forms


# 靓号管理函数.
def pretty_list(req):
    """靓号列表"""
    # addData()
    term = {}
    kw = req.GET.get("kw", "")
    if kw:
        term["mobile__contains"] = kw

    pretty_data = models.PrettyNumber.objects.filter(**term).order_by("-level")
    page_obj = Pagination(req, pretty_data)
    page_query_set = page_obj.page_queryset
    # 分页功能
    page_str = page_obj.gen_html()
    return render(req, "pretty_list.html", {"pretties": page_query_set, "kw": kw, "page_str": page_str})


def pretty_add(req):
    """新增靓号"""
    if req.method == "GET":
        form = day16forms.PrettyNumberAddForm()
        return render(req, "pretty_add.html", {"form": form})
    # 获取post请求的数据并且进行数据校验
    form = day16forms.PrettyNumberAddForm(data=req.POST)
    if form.is_valid():  # 数据校验成功
        # 保存数据
        form.save(commit=True)
        return redirect("/pretty/list")
    # 校验失败,需要停留在这个页面并且显示错误信息
    return render(req, "pretty_add.html", {"form": form})


def pretty_edit(req, nid):
    """修改靓号"""
    pretty_num = models.PrettyNumber.objects.filter(id=nid).first()
    if req.method == "GET":
        form = day16forms.PrettyNumberEditForm(instance=pretty_num)
        return render(req, "pretty_edit.html", {"form": form})  # 使用了验证器,这里就不要传递nid,获取不到的.
    # 获取post请求的数据并且进行数据校验
    form = day16forms.PrettyNumberEditForm(data=req.POST, instance=pretty_num)
    if form.is_valid():  # 数据校验成功
        # 保存数据
        form.save(commit=True)
        return redirect("/pretty/list")
    # 校验失败,需要停留在这个页面并且显示错误信息
    return render(req, "pretty_edit.html", {"form": form})


def pretty_del(req, nid):
    models.PrettyNumber.objects.filter(id=nid).delete()
    return redirect("/pretty/list/")
