import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from day16app import models  # 导入models因为以后可能里面会有很多类不能一个一个导入
from django import forms
from day16app.utils.basemform import BootstrapForm, BootstrapModelForm
from day16app.utils.pagination import Pagination
import os


def city_list(req):
    #查询所有城市数据
    cities = models.City.objects.all()
    # 进行分页处理
    # 1.初始化分页组件
    page_obj = Pagination(req,cities,page_size=8)
    # 2.获取分页数据
    cities_data = page_obj.page_queryset
    # 3.生成分页代码
    page_str = page_obj.gen_html()
    # 4.封装到一个context字典
    context = {
        "cities":cities_data,
         "page_str":page_str
    }
    #渲染数据
    return render(req, "city_list.html", context)


class CityUploadModelForm(BootstrapModelForm):
    bootstrap_exclude_fields = ["img"]

    class Meta:
        model = models.City
        fields = "__all__"


def city_add(req):
    form = CityUploadModelForm()
    if req.method == 'GET':
        return render(req, "upload_form.html", {"form": form, "title": "新增城市"})
    form = CityUploadModelForm(data=req.POST, files=req.FILES)  # 文件上传的时候需要传递数据给files参数
    # 表单验证
    if form.is_valid():
        print(form.cleaned_data)
        form.save()  # 这就是使用ModelForm的好处,直接定义save()方法,就会把图片保存到media/city/里面,把其他数据和图片路径保存到数据库
        return redirect("/city/list/")
    return render(req, "upload_form.html", {"form": form, "title": "新增城市"})
