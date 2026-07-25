from django.db import models


# Create your models here.
class Department(models.Model):
    """部门表"""
    # id = models.BigAutoField(verbose_name="ID",primary_key=True)  #不需要写django会自动处理这个表字段
    title = models.CharField(verbose_name="标题", max_length=32)


class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name="姓名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄", default=18)  # 需要添加默
    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name="入职时间")
    # 这个类型不对,它是没有约束的
    # dep_id=models.BigIntegerField(verbose_name="部门ID")
    # 这个类型有约束的,也就是外键
    # 只需要写dep,然后django会把它变为dep_id
    # 方式1,需要设置关联的表(类),还要设置表的关联的列,还需要设置部门被删除了,对应的员工数据会级联删除.
    dep = models.ForeignKey(to="Department", to_field="id",on_delete=models.CASCADE)
    # 方式2.需要设置关联的表(类),还要设置表的关联的列,还需要设置可以置空,也就是部门被删除了,对应员工的部门变为空
    # dep = models.ForeignKey(to="Department", to_field="id",null=True,blank=True, on_delete=models.SET_NULL)
    gender_choices = (
        (0,"女"),
        (1,"男")
    )
    gender = models.SmallIntegerField(verbose_name="性别",choices=gender_choices) # 注意django中性别的处理方式


