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


def upload_list(req):
    if req.method == "GET":
        return render(req,"upload_list.html")
    print(req.POST)
    print(req.FILES)
    file_obj = req.FILES.get("avatar")
    print(file_obj.name) # 用name属性来获取文件名
    # 保存文件内容
    f = open(file_obj.name,mode='wb')
    for chunk in file_obj.chunks():
        f.write(chunk)
    f.close()
    return HttpResponse("上传成功")
