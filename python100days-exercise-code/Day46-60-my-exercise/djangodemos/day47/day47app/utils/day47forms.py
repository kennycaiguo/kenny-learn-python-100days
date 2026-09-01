from django.forms import widgets
"""
把所有表单相关的类都放在这里,方便views.py的函数调用,而且不会使得views.py过于臃肿
"""
from pyexpat import model

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from day47app.utils.basemodelform import BootstrapModelForm
from django import forms
from day47app import models
from day47app.models import Admin, UserInfo, Department
from day47app.utils.encrypt import md5


# 使用django ModelForm组件的写法
# 1.定义一个表单类继承自forms.ModelForm
class UserInfoForm(BootstrapModelForm):
    """添加用户和编辑用户信息需要使用的类"""
    name = forms.CharField(min_length=2, label="姓名")  # 设置姓名的最小长度
    # 为了不让用户看到密码，我们需要把它密码用"."或者"*"显示
    password = forms.CharField(label="密码",widget=forms.PasswordInput(render_value=True)) # 注意：render_value=False,密码框就为空
    create_time = forms.CharField(
        min_length=10, label="入职时间",
        widget=forms.TextInput(attrs={"autocomplete": "off"})
    )

    class Meta:
        model = UserInfo
        fields = ['name', "password", "age", "account", "create_time", "gender", "dep"]
        


# 操作PrettyNumber添加数据的ModelForm类
class PrettyNumberAddForm(BootstrapModelForm):
    # 添加验证器方式1. 正则表达式 ,验证手机号格式
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')]
    )

    class Meta:
        model = models.PrettyNumber
        # fields = ['mobile', "price", "level", "status"]
        fields = "__all__"  # 也可以这么写,表示模型中所有的字段都需要

    # # 添加验证方式2,钩子函数,验证手机号码是否已经存在,(当然也可以验证手机号格式,这里不是验证手机号格式)
    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]
        exist = models.PrettyNumber.objects.filter(mobile=txt_mobile).exists()
        if exist:
            raise ValidationError("手机号已经存在,不能重复")  # 验证失败就抛异常
        return txt_mobile  # 验证通过就把他返回


# 编辑靓号功能需要用到的类
class PrettyNumberEditForm(BootstrapModelForm):
    # 添加验证器方式1. 正则表达式 ,验证手机号格式
    # mobile = forms.CharField(
    #     label="手机号",
    #     validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')],
    #     disabled=True  # 不允许编辑手机号
    # )
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')],
        disabled=False  # 允许编辑手机号
    )

    class Meta:
        model = models.PrettyNumber
        # fields = ['mobile', "price", "level", "status"]
        fields = "__all__"  # 也可以这么写,表示模型中所有的字段都需要

    # # 添加验证方式2,钩子函数,验证手机号格式的另外一种方式
    # def clean_mobile(self):
    #     txt_mobile = self.cleaned_data["mobile"]
    #     if len(txt_mobile) !=11:
    #         raise ValidationError("手机号格式错误")  # 验证失败就抛异常
    #     return txt_mobile  # 验证通过就把他返回

    # 排除自己以外,手机号不能重复(有点绕,慢慢体会)
    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]
        exist = models.PrettyNumber.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exist:
            raise ValidationError("手机号已经存在,不能重复")  # 验证失败就抛异常
        return txt_mobile  # 验证通过就把他返回

# 添加管理员表单
class AdminAddForm(BootstrapModelForm):
    confirm_pwd = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput
    )
    class Meta:
        model = Admin
        # fields = "__all__"
        fields = ["username","password","confirm_pwd"]
        widgets = {
            "password":forms.PasswordInput # 有错误不清空文本框的内容，其实清空更好
        }


    # 管理员账号不能重复
    def clean_username(self):
        txt_username = self.cleaned_data['username']
        exist = Admin.objects.filter(username=txt_username).exists()
        if exist:
            raise ValidationError("管理员用户名不能重复")
        return txt_username
    
    # 密码加密钩子函数
    def clean_password(self):
        password = self.cleaned_data['password']
        return md5(password)
        
    # 确认密码的钩子
    def clean_confirm_pwd(self):
        txt_pwd = self.cleaned_data["password"] # 此时密码已经加密
        txt_confirm_pwd = md5(self.cleaned_data['confirm_pwd'])
        if txt_pwd !=txt_confirm_pwd:
            raise ValidationError("两次输入的密码不一样")
        return txt_confirm_pwd
    
    


class AdminEditForm(BootstrapModelForm):
    class Meta:
        model = Admin
        fields = '__all__'    

    # 管理员用户不能重复
    def clean_username(self):
        txt_username = self.cleaned_data['username']   
        exists = Admin.objects.exclude(id=self.instance.pk).filter(username=txt_username).exists()
        if exists:
            raise ValidationError("管理员用户名已经存在,请使用不同的用户名")
        return txt_username

class AdminResetForm(BootstrapModelForm):
    confirm_pwd = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )    
    class Meta:
        model = Admin
        fields = ["password", "confirm_pwd"]
        widgets={
            "password":forms.PasswordInput(render_value=True)
        }
        # 注意django处理字段是按照我们设置的顺序来处理的,所以密码的钩子函数一定要写在确认密码的钩子函数之前,否则会有问题.

    def clean_password(self):
        password = self.cleaned_data['password']
        md5_pwd = md5(password) 
        # 然后去数据库看看当前的密码和新输入的密码是否一致,如果一致就不允许。
        old_pwd = Admin.objects.filter(id=self.instance.pk).first().password
        if old_pwd == md5_pwd:
            raise ValidationError("重置密码不能和用来的密码一样！")
        return md5_pwd

    # 重置密码的钩子
    def clean_confirm_pwd(self):
        password = self.cleaned_data.get('password')
        confirm_pwd = md5(self.cleaned_data['confirm_pwd'])
        if password != confirm_pwd:
            raise ValidationError("两次输入的密码不一样")
        return confirm_pwd
