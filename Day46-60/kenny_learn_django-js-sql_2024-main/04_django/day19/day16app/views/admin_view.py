from django.shortcuts import render, redirect
from day16app import models  # 导入models因为以后可能里面会有很多类不能一个一个导入
from day16app.utils.pagination import Pagination
from day16app.utils import day16forms


def admin_list(req):
    # session信息校验,检查用户是否已经登录
    info = req.session.get("info")
    if not info:  # 用户没有登录
        return redirect("/login")
    # 搜索功能
    term = {}
    kw = req.GET.get("kw", "")
    if kw:
        term["username__contains"] = kw

    admins = models.Admin.objects.filter(**term)
    # 分页
    # 1.实例化分页类的对象
    page_obj = Pagination(req, admins, page_size=8)
    # 2.获取分页数据
    page_query_set = page_obj.page_queryset
    # 3.获取分页器的html字符串
    page_str = page_obj.gen_html()
    return render(req, "admin_list.html", {"admins": page_query_set, "kw": kw, "page_str": page_str})


def admin_add(req):
    # 新增管理员
    if req.method == 'GET':
        form = day16forms.AdminAddForm()
        return render(req, "add_or_edit.html", {"form": form, "title": "新增管理员"})
    # 获取post请求的数据并且进行数据校验
    form = day16forms.AdminAddForm(data=req.POST)
    if form.is_valid():  # 数据校验成功
        # 保存数据
        form.save(commit=True)
        return redirect("/admin/list")
    # 校验失败,需要停留在这个页面并且显示错误信息
    return render(req, "add_or_edit.html", {"form": form, "title": "新增管理员"})


def admin_edit(req, nid):
    """修改管理员"""
    # 先确保用户传递过来的id有效
    admin1 = models.Admin.objects.filter(id=nid).first()
    # 需要先检查这个id是否存在
    if not admin1:
        # return redirect("/admin/list/") # 如果nid不存在,这个查询结果是None,我们就把它重定向到管理员列表里面
        return render(req, "error.html", {"msg": f"没有id为{nid}的管理员"})  # 如果nid不存在,这个查询结果是None,我们就渲染错误页面
    if req.method == "GET":
        form = day16forms.AdminEditForm(instance=admin1)
        return render(req, "add_or_edit.html", {"form": form, "title": "修改管理员"})  # 使用了验证器,这里就不要传递nid,获取不到的.
    # 获取post请求的数据并且进行数据校验
    form = day16forms.AdminEditForm(data=req.POST, instance=admin1)
    if form.is_valid():  # 数据校验成功
        # 保存数据
        form.save(commit=True)
        return redirect("/admin/list")
    # 校验失败,需要停留在这个页面并且显示错误信息
    return render(req, "add_or_edit.html", {"form": form, "title": "修改管理员"})


def admin_reset(req, nid):
    # 先确保用户传递过来的id有效
    admin1 = models.Admin.objects.filter(id=nid).first()
    # 需要先检查这个id是否存在
    if not admin1:
        # return redirect("/admin/list/") # 如果nid不存在,这个查询结果是None,我们就把它重定向到管理员列表里面
        return render(req, "error.html", {"msg": f"没有id为{nid}的管理员"})  # 如果nid不存在,这个查询结果是None,我们就渲染错误页面
    if req.method == "GET":
        form = day16forms.AdminResetForm()
        return render(req, "add_or_edit.html",
                      {"form": form, "title": f"重置管理员-{admin1.username}"})  # 使用了验证器,这里就不要传递nid,获取不到的.
    form = day16forms.AdminResetForm(data=req.POST, instance=admin1)
    if form.is_valid():  # 数据校验成功
        # 保存数据
        form.save(commit=True)
        return redirect("/admin/list")
    # 校验失败,需要停留在这个页面并且显示错误信息
    return render(req, "add_or_edit.html", {"form": form, "title": f"重置管理员-{admin1.username}"})


def admin_del(req, nid):
    # 保证nid存在
    admin = models.Admin.objects.filter(id=nid).first()
    if not admin:
        return redirect("/admin/list/")  # 如果不存在,就跳转到管理员列表
    admin.delete()
    return redirect("/admin/list/")
