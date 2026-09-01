from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from day47app.addnum import addData
from day47app.models import PrettyNumber
from day47app.utils.pagination import Pagination

class PrettyNumForm(forms.ModelForm):
    # 添加验证器方式1
    mobile = forms.CharField(
        label='手机号',
        validators=[RegexValidator(r'^1[3-9]\d{9}','手机号格式错误')]
    )
    class Meta:
        model = PrettyNumber
        fields = '__all__'
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs={"class":"form-control","placeholder":field.label}

    # 使用抛异常的方法来验证手机号是否重复不是一个好方法,我们可以在models.py中给PrettyNumber类的mobile字段的定义里面添加一个unique=True即可
    #         
    # # 添加验证器方式2，创建一个clean_字段名函数
    # 这里我们用clean_xx函数来解决修改后的手机号和另外一个用户的手机号重复的问题
    # def clean_mobile(self):
    #     txt_mobile = self.cleaned_data['mobile']
    #     exist = PrettyNumber.objects.filter(mobile=txt_mobile).exists()
    #     if exist:
    #         raise ValidationError("手机号已经存在")
    #         # return ValidationError("手机号已经存在")
        
    #     return txt_mobile



def pretty_list(req):
    # addData() #just for test purpose
    term = {} 
    kw = req.GET.get('kw','')
    if kw:
        term['mobile__contains'] = kw
    pretty_nums = PrettyNumber.objects.filter(**term).order_by("-level")
    page_obj = Pagination(req,pretty_nums)
    page_queryset = page_obj.page_queryset
    # 分页数据
    page_str = page_obj.gen_html()

    return render(req,'pretty_list.html',{"pretty_nums":page_queryset,"kw":kw,"page_str":page_str})

def pretty_add(req):
    title = "新增靓号"
    # get method
    if req.method == 'GET':
        form = PrettyNumForm()
        return render(req,"pretty_add_edit.html",{"form":form,"title":title})
    # post method
    form = PrettyNumForm(data=req.POST)
    if form.is_valid():
        form.save()
        return redirect("/pretty/list/")
    return  render(req,"pretty_add_edit.html",{"form":form,"title":title})

def pretty_edit(req,nid):
    # 处理id无效的情况
    row = PrettyNumber.objects.filter(id=nid)
    if not row:
        return redirect("/pretty/list/")
    title = "编辑靓号"
    num = PrettyNumber.objects.filter(id=nid).first()
    print(num)
    # handle get
    if req.method == 'GET':
        form = PrettyNumForm(instance=num)
        return render(req,'pretty_add_edit.html',{"form":form,"title":title})
    # handle post method
    form = PrettyNumForm(data=req.POST,instance=num)
    if form.is_valid():
        form.save()
        return redirect('/pretty/list/')
    return render(req,'pretty_edit.html',{"form":form,"title":title})

def pretty_del(req,nid):
    PrettyNumber.objects.filter(id=nid).delete()
    return redirect("/pretty/list/")
