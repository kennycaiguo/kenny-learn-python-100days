from django.shortcuts import render, redirect
from day16app import models  # 导入models因为以后可能里面会有很多类不能一个一个导入
from day16app.utils.pagination import Pagination
from day16app.utils import day16forms


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
        return render(req, "add_or_edit.html", {"form": form, "title": "添加靓号"})
    # 获取post请求的数据并且进行数据校验
    form = day16forms.PrettyNumberAddForm(data=req.POST)
    if form.is_valid():  # 数据校验成功
        # 保存数据
        form.save(commit=True)
        return redirect("/pretty/list")
    # 校验失败,需要停留在这个页面并且显示错误信息
    return render(req, "add_or_edit.html", {"form": form})


def pretty_edit(req, nid):
    """修改靓号"""
    # 保证nid是存在的
    pretty_num = models.PrettyNumber.objects.filter(id=nid).first()
    if not pretty_num:
        # return redirect("/pretty/list/")   # 方式1 重定向
        return render(req, "error.html",{"msg":f"没有id为{nid}的靓号"})  # 方式2 展示错误页面
    if req.method == "GET":
        form = day16forms.PrettyNumberEditForm(instance=pretty_num)
        return render(req, "add_or_edit.html", {"form": form, "title": "修改靓号"})  # 使用了验证器,这里就不要传递nid,获取不到的.
    # 获取post请求的数据并且进行数据校验
    form = day16forms.PrettyNumberEditForm(data=req.POST, instance=pretty_num)
    if form.is_valid():  # 数据校验成功
        # 保存数据
        form.save(commit=True)
        return redirect("/pretty/list")
    # 校验失败,需要停留在这个页面并且显示错误信息
    return render(req, "add_or_edit.html", {"form": form, "title": "修改靓号"})


def pretty_del(req, nid):
    # 保证nid是有效的
    pretty = models.PrettyNumber.objects.filter(id=nid).first()
    if not pretty:
        return redirect("/pretty/list/") # 如果nid不存在,就跳转到靓号列表
    pretty.delete()
    return redirect("/pretty/list/")
