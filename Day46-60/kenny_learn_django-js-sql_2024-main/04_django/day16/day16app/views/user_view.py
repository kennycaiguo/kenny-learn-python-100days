from django.shortcuts import render, redirect
from day16app import models  # 导入models因为以后可能里面会有很多类不能一个一个导入
from day16app.utils.pagination import Pagination
from day16app.form import day16forms


def user_list(req):
    users = models.UserInfo.objects.all()
    # 分页
    # 1.实例化分页类的对象
    page_obj = Pagination(req, users, page_size=3)
    # 2.获取分页数据
    page_query_set = page_obj.page_queryset
    # 3.获取分页器的html字符串
    page_str = page_obj.gen_html()
    # 渲染数据
    return render(req, "user_list.html", {'users': page_query_set, "page_str": page_str})


def user_add(req):
    """新增用户"""
    if req.method == "GET":
        form = day16forms.UserInfoForm()
        return render(req, "user_add.html", {"form": form})
    # 获取post请求的数据并且进行数据校验
    form = day16forms.UserInfoForm(data=req.POST)
    if form.is_valid():  # 数据校验成功
        # 保存数据
        form.save(commit=True)
        return redirect("/user/list")
    # 校验失败,需要停留在这个页面并且显示错误信息
    return render(req, "user_add.html", {"form": form})




def user_edit(req, nid):
    """编辑用户信息"""
    # 查询数据
    user1 = models.UserInfo.objects.filter(id=nid).first()  # 放在这里是因为有2个地方需要用到这个user1
    if req.method == "GET":
        form = day16forms.UserInfoForm(instance=user1)
        return render(req, "user_edit.html", {"form": form, "nid": nid})
    # 获取post请求的数据并且进行数据校验
    form = day16forms.UserInfoForm(instance=user1, data=req.POST)  # 更新的时候需要两个参数来构造form对象:数据和需要更新的实例
    if form.is_valid():  # 数据校验成功
        # 保存数据
        form.save()  # 新增和更新都是使用这个方法,只是form里面的数据不一样
        return redirect("/user/list")
    # 校验失败,需要停留在这个页面并且显示错误信息
    return render(req, "user_edit.html", {"form": form})


def user_del(req, nid):
    """删除用户信息"""
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")

