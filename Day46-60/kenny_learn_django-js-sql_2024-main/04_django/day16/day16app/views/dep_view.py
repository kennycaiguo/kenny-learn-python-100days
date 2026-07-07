from django.shortcuts import render, redirect
from day16app import models  # 导入models因为以后可能里面会有很多类不能一个一个导入
from day16app.utils.pagination import Pagination


def dep_list(req):
    """显示部门列表"""
    dep_list = models.Department.objects.all()
    # 分页功能实现
    # 1.实例化分页组件
    page_obj = Pagination(req, dep_list, page_size=2)
    # 2.获取分页后的数据
    page_query_set = page_obj.page_queryset
    # 3.获取分页器的html字符串
    page_str = page_obj.gen_html()
    # 渲染数据
    return render(req, "dep_list.html", {"deps": page_query_set, "page_str": page_str})


def dep_add(req):  # 这个功能太简单了,只有一个字段,不需要ModelForm
    """新增部门"""
    # get
    if req.method == "GET":
        return render(req, "dep_add.html")
    # post
    title = req.POST.get("title")
    models.Department.objects.create(title=title)
    return redirect("/dep/list")


def dep_del(req):
    """删除部门"""
    nid = req.GET.get("nid")
    models.Department.objects.filter(id=nid).delete()
    return redirect("/dep/list")


def dep_edit(req, nid):
    # 处理get
    if req.method == "GET":
        dep = models.Department.objects.filter(id=nid).first()
        return render(req, "dep_edit.html", {"dep": dep})
    # 处理post
    # id T= req.POS.get("id")  # 在模板里面没有使用hidden字段,这里就不需要这一句
    title = req.POST.get("title")
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect("/dep/list")
