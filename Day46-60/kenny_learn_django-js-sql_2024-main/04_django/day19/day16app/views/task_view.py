import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from day16app import models  # 导入models因为以后可能里面会有很多类不能一个一个导入
from day16app.utils.encrypt import md5
from day16app.utils.pagination import Pagination
from day16app.utils.day16forms import TaskModelForm
from day16app.utils.code import check_code
from io import BytesIO
from django import forms
from day16app.utils.basemform import BootstrapForm


def task_list(req):
    # 获取所有任务
    tasks = models.Task.objects.all().order_by("-id")
    # 分页
    # 1.实例化分页类的对象
    page_obj = Pagination(req, tasks, page_size=3)
    # 2.获取分页数据
    page_query_set = page_obj.page_queryset
    # 3.获取分页器的html字符串
    page_str = page_obj.gen_html()
    # 用TaskModelForm生成表单对象
    form = TaskModelForm()
    # 在面板html中渲染数据
    return render(req, "task_list.html", {"form": form, "tasks": page_query_set, "page_str": page_str})


def task_test_list(req):
    return render(req, "task_test_list.html")


@csrf_exempt
def task_test_ajax(req):
    # 这里获取get请求的参数然后返回给用户
    # n1 = req.GET.get("n1")
    # n2 = req.GET.get("n2")
    # 获取post请求参数
    n1 = req.POST.get("n1")
    n2 = req.POST.get("n2")
    data_dict = {"status": "ok", "data": {"n1": n1, "n2": n2}}

    # return HttpResponse(json.dumps(data_dict))
    return JsonResponse(data_dict)


# 响应ajax带表单的请求
@csrf_exempt
def task_test_ajax2(req):
    print(req.POST)
    data_dict = {"status": "ok", "data": req.POST}
    return HttpResponse(json.dumps(data_dict))
    # return JsonResponse(req.POST) #这个有时候比如这里是不好用的.还是上面的好用


@csrf_exempt
def task_add(req):
    print(req.POST)
    # 表单数据校验
    form = TaskModelForm(data=req.POST)
    if form.is_valid():
        # 校验成功就保存数据
        form.save()
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))
    # 验证失败,返回一个包含错误信息的json字符串
    data_dict = {"status": False, "errors": form.errors}
    return HttpResponse(json.dumps(data_dict, ensure_ascii=False))
