from ast import If

from django import forms



from day47app.models import UserInfo,Department
from django.shortcuts import render,redirect
from django.http import HttpResponse

from day47app.utils.pagination import Pagination

def user_list(req):
    users = UserInfo.objects.all()
    # 分页
    # 1.实例化分页类的对象
    page_obj = Pagination(req,users,page_size=3)
    # 2.获取分页数据
    page_queryset = page_obj.page_queryset
    # 3.获取分页器的html字符串
    page_str = page_obj.gen_html()
    return render(req,'user_list.html',{'users':page_queryset,"page_str":page_str})


class MyForm(forms.ModelForm):
    name = forms.CharField(min_length=3,label='姓名')
    class Meta:
        model = UserInfo
        fields = ['name','password','age','account','create_time','gender','dep']
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs={"class":"form-control","placeholder":field.label}

       

def user_add(req):
    if req.method == 'GET':
        form = MyForm()
        return render(req,'user_add.html',{'form':form})
    # method post
    form = MyForm(req.POST)
    # VERIFY
    if form.is_valid():
        form.save(commit=True)
        return redirect("/user/list")
    return render(req,'user_add.html',{'form':form})  

def user_edit(req,nid):
    # get method handling
    user = UserInfo.objects.filter(id=nid).first()
    if req.method == "GET":
        form = MyForm(instance=user)
        return render(req,"user_edit.html",{"form":form})
    # post method data handling
    # print(req.POST)
    form = MyForm(instance=user,data=req.POST)
    if form.is_valid():
        form.save()
        return redirect("/user/list/")   
    return render(req,"user_edit.html",{"form":form})

def user_del(req):
    nid = req.GET.get('nid')
    # print(nid)
    UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')