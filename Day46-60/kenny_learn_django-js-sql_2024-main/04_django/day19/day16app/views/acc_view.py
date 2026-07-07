from django.http import HttpResponse
from django.shortcuts import render, redirect
from day16app import models  # 导入models因为以后可能里面会有很多类不能一个一个导入
from day16app.utils.encrypt import md5
from day16app.utils.pagination import Pagination
from day16app.utils import day16forms
from day16app.utils.code import check_code
from io import BytesIO
from django import forms
from day16app.utils.basemform import BootstrapForm


class LoginForm(BootstrapForm):
    # 这里的字段名一定要和表单里面的name一样,并且要和Admin类里面的字段名一样,否则后面很难操作
    username = forms.CharField(label="用户名", widget=forms.TextInput)
    password = forms.CharField(label="密 码",widget=forms.PasswordInput(attrs={"autocomplete": "off"}, render_value=True))
    code = forms.CharField(label="验证码", widget=forms.TextInput(attrs={"autocomplete": "off"}),required=True)

    def clean_password(self):
        txt_pwd = self.cleaned_data.get("password")
        return md5(txt_pwd)  # 把获取到的密码进行md5加密


def login(req):
    if req.method == "GET":
        form = LoginForm()
        return render(req, "login.html", {"form": form})
    form = LoginForm(data=req.POST)
    if form.is_valid():
        # 验证码校验,这里需要用到一个小技巧,调用form.clean_data.pop(xxx)方法
        user_input_code = form.cleaned_data.pop('code')  # 这里需要使用pop是因为我们的数据库里面没有code,而我们下面需要用form的字段去数据库中校验,这样子会有问题
        code = req.session.get("image_code", "")
        if user_input_code.upper() != code.upper():
            form.add_error("code", "验证码错误")
            return render(req, "login.html", {"form": form})  # 验证码错误不允许跳转还得停留在登录页面
        # 普通form是没有save方法的,注意modelform才有
        # 写法1,
        # user = form.cleaned_data.get("username")
        # pwd = form.cleaned_data.get("password")
        # admin = models.Admin.objects.filter(username=user,password=pwd).first()

        # 写法2
        admin = models.Admin.objects.filter(**form.cleaned_data).first() # 验证码校验通过,再进行用户名和密码校验
        # 如果用户名或者密码错误,就找不到数据.在渲染登录页面,也就是不让他跳转
        if not admin:
            form.add_error("password", "用户名或者密码错误!!!")  # 这个方法不需要修改模板的内容
            return render(req, "login.html", {"form": form})  # 用户信息验证失败,也就是登录失败
            # return render(req, "login.html", {"form": form,"error_msg":"用户名或者密码错误"})
        # 登录成功,生成随机字符串写到用户浏览器的cookie中,在django中这个操作比较简单.
        req.session["info"] = {"id": admin.id, "name": admin.username}
        req.session.set_expiry(60*60*24*7) # 设置用户7天免登录,这个其实可以根据你自己的需求来设置
        return redirect("/admin/list/")  # 登录成功,跳转到管理员账户页面
    return render(req, "login.html", {"form": form})  # form表单校验失败


def logout(req):
    """注销功能"""
    # 注销也很简单,就是把session的数据清空
    req.session.clear()
    # 然后重定向到登录页面
    return redirect("/login/")


def image_code(req):
    '''生成图片验证码'''
    img, code_str = check_code()
    print(code_str)
    # 把生成的验证码保存到session
    req.session["image_code"] = code_str
    # 还要设置session的过期时间
    req.session.set_expiry(60)
    stream = BytesIO()
    img.save(stream, "png")
    return HttpResponse(stream.getvalue())
