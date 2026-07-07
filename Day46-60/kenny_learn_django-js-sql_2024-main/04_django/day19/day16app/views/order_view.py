import json
import random
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from day16app import models  # 导入models因为以后可能里面会有很多类不能一个一个导入
from day16app.utils.encrypt import md5
from day16app.utils.pagination import Pagination
from day16app.utils.day16forms import OrderModelForm
from day16app.utils.code import check_code
from io import BytesIO
from django import forms
from day16app.utils.basemform import BootstrapForm


def order_list(req):
    # 获取所有数据
    orders = models.Order.objects.all().order_by("-id")  # 倒序排列
    # 分页
    page_obj = Pagination(req, orders, page_size=5)
    page_query_set = page_obj.page_queryset
    # 分页功能
    page_str = page_obj.gen_html()
    form = OrderModelForm()
    context = {
        "form": form,
        "orders": page_query_set,
        "page_str": page_str
    }
    # 渲染数据
    return render(req, "order_list.html", context)


@csrf_exempt
def order_add(req):
    """新增订单的后台处理函数Ajax提交方式"""
    print(req.POST)
    form = OrderModelForm(data=req.POST)
    if form.is_valid():
        # 生成oid并且添加到form的数据中
        oid = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999))
        form.instance.oid = oid
        # 从session在获取当前登录的管理员的id
        # admin =req.session.get("info")
        # # print(req.session.get("info"))
        # form.instance.admin_id = admin.get("id")
        form.instance.admin_id = req.session["info"]["id"]  # 也可以这么写
        form.save()  # 表单验证(主要是不让数据为空)通过,就保存数据

        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))
    data_dict = {"status": False, "errors": form.errors}
    return HttpResponse(json.dumps(data_dict))  # 验证失败就返回错误信息


# 这个是get请求,不需要csrf_token免除,只有post请求才需要
def order_del(req):
    # 获取用户传递过来的id
    did = req.GET.get("did")
    print(did)
    # 校验一下需要删除的数据是否在数据库中存在
    if not models.Order.objects.filter(id=did).exists():
        data_dict = {"status": False, "errors": "删除失败,没有找到需要删除的数据"}
        return JsonResponse(data_dict)
    # 删除数据,
    models.Order.objects.filter(id=did).delete()
    data_dict = {"status": True}
    return JsonResponse(data_dict)


# 处理Ajax根据id进行查询的请求
def order_detail(req):
    # #方式1
    # eId = req.GET.get("eId")
    # orders = models.Order.objects.filter(id=eId)
    # # orders = models.Order.objects.filter(id=10000)
    # if not orders.exists():
    #     data_dict = {"status": False, "errors": "查询失败,没有数据"}
    #     return JsonResponse(data_dict)
    # order = orders.first()
    # data_dict = {"status": True, "data": {"id":order.id,"oid":order.oid,"title":order.title,"price":order.price,
    #                                                                          "status":order.status,"admin_id":order.admin.id}}
    # # data_dict = {"status": True, "data":order}
    # return HttpResponse(json.dumps(data_dict))

    ## 方式2
    eId = req.GET.get("eId")
    order_dict = models.Order.objects.filter(id=eId).values("title", "price", "status").first()
    if not order_dict:
        data_dict = {"status": False, "errors": "查询失败,没有数据"}
        return JsonResponse(data_dict)
    data_dict = {"status": True, "data": order_dict}

    return JsonResponse(data_dict)


@csrf_exempt
def order_edit(req, eId):
    """编辑订单的后台处理函数Ajax提交方式"""
    print(eId)
    order = models.Order.objects.filter(id=eId).first()
    print(order)
    # print(req.POST)
    form = OrderModelForm(data=req.POST, instance=order)
    if form.is_valid():
        form.save()  # 表单验证(主要是不让数据为空)通过,就保存数据

        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))
    data_dict = {"status": False, "errors": form.errors}
    return HttpResponse(json.dumps(data_dict))  # 验证失败就返回错误信息


@csrf_exempt
def order_edit2(req):
    """编辑订单的后台处理函数Ajax提交方式"""
    eId = req.GET.get("eId")
    print(eId)
    order = models.Order.objects.filter(id=eId).first()
    if not order:
        data_dict={"status":False,"errorMsg":"没有你要找的数据"}
        return JsonResponse(data_dict)
    print(order)
    # print(req.POST)
    form = OrderModelForm(data=req.POST, instance=order)
    if form.is_valid():
        form.save()  # 表单验证(主要是不让数据为空)通过,就保存数据

        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))
    data_dict = {"status": False, "errors": form.errors}
    return HttpResponse(json.dumps(data_dict))  # 验证失败就返回错误信息
