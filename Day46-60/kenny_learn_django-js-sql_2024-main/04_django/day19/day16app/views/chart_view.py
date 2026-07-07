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


def chart_list(req):
    return render(req, "chart_list.html")


def chart_bar(req):
    """构造柱状图数据"""
    # 这里我们用一个列表来模拟从数据库里面获取数据
    legend = ["Jack", "Mary"]
    series_list = [
        {
            "name": 'Jack',
            "type": 'bar',
            "data": [5, 20, 36, 10, 10, 20]
        },
        {
            "name": 'Mary',
            "type": 'bar',
            "data": [3, 8, 26, 15, 7, 30]
        }
    ]
    x_axis = ['1月', '2月', '3月', '4月', '5月', '6月']

    result = {
        "status": True,
        "data": {
            "legend": legend,
            "series_list": series_list,
            "x_axis": x_axis,
        }
    }

    return JsonResponse(result)


def chart_pie(req):
    """"构造饼状图数据"""
    data_list = [
        {"value": 1048, "name": '研发部'},
        {"value": 735, "name": '财务部'},
        {"value": 580, "name": '采购部'},
        {"value": 580, "name": '维修部'}
    ]

    result = {
        "status": True,
        "data": data_list
    }

    return JsonResponse(result)


def chart_line(req):
    """构造折线图数据"""
    legend=['上海分公司', '广东分公司', '云南分公司']
    x_axis = ['1月', '2月', '3月', '4月', '5月', '6月','7月']
    series_list = [
                {
                  "name": '上海分公司',
                  "type": 'line',
                  "stack": 'Total',
                  "data": [120, 132, 101, 134, 90, 230, 210]
                },
                {
                  "name": '广东分公司',
                  "type": 'line',
                  "stack": 'Total',
                  "data": [220, 182, 191, 234, 290, 330, 310]
                },
                {
                  "name": '云南分公司',
                  "type": 'line',
                  "stack": 'Total',
                  "data": [150, 232, 201, 154, 190, 330, 410]
                }
    ]

    date_dict = {
        "legend":legend,
        "x_axis":x_axis,
        "series_list":series_list
    }

    result = {
        "status":True,
        "data":date_dict
    }
    return JsonResponse(result)