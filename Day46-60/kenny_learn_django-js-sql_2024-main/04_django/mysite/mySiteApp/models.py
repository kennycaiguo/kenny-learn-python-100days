from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=1)  # 需要添加默认值

    # size = models.IntegerField()  # 生成了表后再添加字段会有问题,需要你做一个选择
    # data = models.IntegerField(null=True,blank=True)  #允许为空,也是没有问题的


class Department(models.Model):
    title = models.CharField(max_length=16)


# 给部门表添加数据,使用类的create方法
# Department.objects.create(title="销售部")
