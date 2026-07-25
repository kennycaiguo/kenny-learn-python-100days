from django.http import HttpResponse
from django.shortcuts import render,redirect

from day47app.models import Department


def dep_home(request):
    return redirect("list/")
def dep_list(request):
    deps = Department.objects.all()
    return render(request,"dep_list.html",{"deps":deps})


def dep_add(request):
    if request.method == "GET":
        return render(request,'dep_add.html')
    title = request.POST.get("title")
    Department.objects.create(title=title)
    return HttpResponse("添加数据成功")


def dep_del(request):
    nid = request.GET.get("nid")
    print(nid)
    Department.objects.filter(id=nid).delete()
    return redirect("/dep/list")

# 匹配dep/edit/?nid=xx
# def dep_edit(request):
#     # 处理get请求
#     if request.method == "GET":
#         nid = request.GET.get("nid")
#         dep = Department.objects.get(id=nid)
#         return render(request,"dep_edit.html",{"dep":dep})
#     # 处理post请求
#     id = int(request.POST.get("id"))
#     title = request.POST.get("title")
#     Department.objects.filter(id=id).update(title=title)
#     return redirect("/dep/list")

# 配置dep/1/edit/
def dep_edit(request,nid):
    # 处理get请求
    if request.method == "GET":
        dep = Department.objects.get(id=nid)
        return render(request,"dep_edit.html",{"dep":dep})
    # 处理post请求
    id = int(request.POST.get("id"))
    title = request.POST.get("title")
    Department.objects.filter(id=id).update(title=title)
    return redirect("/dep/list")

def home(req):
    return render(req,'home.html')