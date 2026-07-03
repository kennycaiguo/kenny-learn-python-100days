# 一.创建应用程序

## 1.创建day47项目，是django项目，

![image-20260629075323558](./django的orm复习笔记.assets/image-20260629075323558.png)

## 2.然后创建day47app应用程序,使用命令：python manage.py day47app

![image-20260629075551232](./django的orm复习笔记.assets/image-20260629075551232.png)

### 注意：需要在day47/settings.py里面注册这个app

![image-20260629091439909](./django的orm复习笔记.assets/image-20260629091439909.png)

## 3.在项目根目录下面创建静态文件路径，把它放在项目的根目录下面，把一些图片，css和js和bootstrap文件放在这里

![image-20260630093756567](./django的orm复习笔记.assets/image-20260630093756567.png)

## 然后在day47/settings.py里面配置这个静态路径

![image-20260630093935873](./django的orm复习笔记.assets/image-20260630093935873.png)

### 配置成功，就可以访问了

![image-20260629080503001](./django的orm复习笔记.assets/image-20260629080503001.png)

# 二.Django的Orm的使用步骤（注意，我们复习项目是day47）

## 1.在day47app/models.py创建对应的类

```
from django.db import models

# Create your models here.
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



```



## 2.创建数据库

```
create database day47 default charset=utf8 collate=utf8_general_ci;
```

![{14CBC9B0-730F-4BFD-AE20-DFA897BB88ED}](./django的orm使用步骤.assets/{14CBC9B0-730F-4BFD-AE20-DFA897BB88ED}.png)

## 3.在day47的settings.py配置数据库连接

```
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'day47',
        'USER':'root',
        'PASSWORD':'root',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }

    #  'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
}
...
```

## 4.然后我们就可以使用orm来迁移数据到数据库

### 4.1打开终端定位到项目根目录，然后输入

```
python manage.py makemigrations
```

![image-20260628083242345](./django的orm复习笔记.assets/image-20260628083242345.png)

### 4.2 然后输入迁移命令: 

```
python manage.py migrate
```

![image-20260628083327847](./django的orm复习笔记.assets/image-20260628083327847.png)

### 数据库建立起来了

![image-20260628083434803](./django的orm复习笔记.assets/image-20260628083434803.png)



# 三.应用程序各个功能的开发

## 3.1我们先从部门功能开始，我们把day47app/views.py删除，然后新建一个views文件夹，凡是dep/XXX/等等的路由都由dep_views.py处理，admin/XXx/等等路由都由admin_views.py处理，以此类推，我们在day47app/views文件夹里面新建一个dep_views.py,先创建一个dep_list函数和一个dep_home函数

![image-20260629113332363](./django的orm复习笔记.assets/image-20260629113332363.png)

## 3.2然后我们回到day47/urls.py,我们的项目的所有路由映射都配置在这里先配置3个路由

![image-20260629113219948](./django的orm复习笔记.assets/image-20260629113219948.png)

### 然后我们来测试一下

![image-20260629112545094](./django的orm复习笔记.assets/image-20260629112545094.png)

## 3.3然后我们需要在day47app/views/dep_view.py里面新建一个dep_list函数，内容如下

![image-20260630075823375](./django的orm复习笔记.assets/image-20260630075823375.png)

## 3.4然后我们需要在templates文件夹里面创建这个dep_list.html文件，内容如下，我们只是创建一个结构，因为此时还没有数据

```
{% load static %}
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>部门列表</title>
    <link rel="stylesheet" href="{% static 'plugins/bootstrap-3.4.1/css/bootstrap.min.css' %}">
    <style>
        .table {
            width: 100%;
        }
        .navbar{
            border-radius: 0;
        }
    </style>
</head>
<body>
{#导航条#}
<nav class="navbar navbar-default">
  <div class="container">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="#">用户管理系统</a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li><a href="/dep/list">部门管理</a></li>
        <li><a href="#">Link</a></li>
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="#">登录</a></li>
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">当前用户名称 <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="#">个人资料</a></li>
            <li><a href="#">我的信息</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">注销</a></li>
          </ul>
        </li>
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
{#主体内容#}
<div class="container">
    <div style="margin-bottom: 5px;">
        <a href="/dep/add/" class="btn btn-primary">
            <span class="glyphicon glyphicon-plus" aria-hidden="true"></span>
            新增部门
        </a>
    </div>
    <div class="panel panel-default">
        <div class="panel-heading">
            <span class="glyphicon glyphicon-th-list" aria-hidden="true"></span>
            部门列表
        </div>
       <table class="table table-bordered table-responsive">
            <thead>
              <tr>
                  <th>ID</th>
                  <th>部门名称</th>
                  <th>操作</th>
              </tr>
              </thead>
            <tbody>
            {% for dep in deps %}
                <tr>
                <td>{{dep.id}}</td>
                <td>{{dep.title}}</td>
                <td>
                    <a class="btn btn-success btn-xs" href="">编辑</a>
                    <a class="btn btn-danger btn-xs" href="/dep/del/?nid={{ dep.id }}">删除</a>
                </td>
                </tr>
            {% endfor %}
            </tbody>
       </table>
    </div>
</div>
<script src="{% static 'js/jquery3.7.1.min.js' %}"></script>
<script src="{% static 'plugins/bootstrap-3.4.1/js/bootstrap.min.js' %}"></script>

</body>
</html>
```

![image-20260630092900823](./django的orm复习笔记.assets/image-20260630092900823.png)

### 运行程序，访问/dep，效果如下

![image-20260630094429194](./django的orm复习笔记.assets/image-20260630094429194.png)



## 3.5我们用navicat往数据库里面添加2条记录

![image-20260630112500764](./django的orm复习笔记.assets/image-20260630112500764.png)

### 刷新网页，数据出来了

![image-20260630112622629](./django的orm复习笔记.assets/image-20260630112622629.png)

## 3.6实现新增功能

### 1>先在day47/urls.py里面添加一条dep/add/路由，把它和day47app/views/dep_view.py里面的dep_add函数建立映射

![image-20260630112950469](./django的orm复习笔记.assets/image-20260630112950469.png)

### 2>然后我们在day47app/views/dep_view.py里面创建dep_add函数

![image-20260630113233227](./django的orm复习笔记.assets/image-20260630113233227.png)

### 3>在day47/templates文件夹里面新建一个dep_add.html文件，内容如下

```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>新增部门</title>
     <link rel="stylesheet" href="{% static 'plugins/bootstrap-3.4.1/css/bootstrap.min.css' %}">
    <style>
        .navbar{
            border-radius: 0;
        }
    </style>
</head>
<body>
<nav class="navbar navbar-default">
  <div class="container">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="#">用户管理系统</a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li><a href="/dep/list">部门管理</a></li>
        <li><a href="#">Link</a></li>
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="#">登录</a></li>
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">当前用户名称 <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="#">个人资料</a></li>
            <li><a href="#">我的信息</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">注销</a></li>
          </ul>
        </li>
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
<div>
    <div class="container">
        <div class="panel panel-default">
          <!-- Default panel contents -->
          <div class="panel-heading">
              <h3 class="panel-title">新建部门</h3>
          </div>
          <div class="panel-body">
          {# 表单  #}
           <form action="/dep/add/" method="post">
              <div class="form-group">
                <label>部门名称</label>
                <div>
                  <input type="text" class="form-control" name="title" placeholder="输入部门">
                </div>
              </div>
              <button type="submit" class="btn btn-success">保 存</button>
        </form>
          </div>
        </div>

    </div>
</div>


  <script src="{% static 'js/jquery3.7.1.min.js' %}"></script>
  <script src="{% static 'plugins/bootstrap-3.4.1/js/bootstrap.min.js' %}"></script>
</body>
</html>


```



#### 注意，这个模板文件的添加路径也/dep/add/,但是提交方式的post，也就是说在django里面同一个路由既可以做get请求，也可以做post请求，我们需要根据提交方式来做不同的处理代码

### 4>此时我们点击部门列表页面的新增按钮，就会打开新增页面，如图![image-20260630114351078](./django的orm复习笔记.assets/image-20260630114351078.png)

### 5>然后我们回到dep_view.py,添加新增部门的代码

![image-20260630114749125](./django的orm复习笔记.assets/image-20260630114749125.png)

### 6>此时我们打开添加页面，添加一个市场部，点击保存，会报错，说没有csrf_token

![image-20260630114857851](./django的orm复习笔记.assets/image-20260630114857851.png)

### 7>解决办法就是在dep_add.html的form表单里面添加一个token标记

![image-20260630114959079](./django的orm复习笔记.assets/image-20260630114959079.png)

#### 然后刷新页面，发现添加数据成功，我们到数据库里面看看，发现的确添加成功

![image-20260630115058375](./django的orm复习笔记.assets/image-20260630115058375.png)

## 3.7实现删除部门功能

### 1）在day47/urls.py里面添加一个dep/del/路由，和day47app/views/dep_view.py里面的dep_del函数映射起来

![image-20260630124121203](./django的orm复习笔记.assets/image-20260630124121203.png)

### 2)然后需要在day47app/views/dep_view.py里面创建dep_del函数，代码如下，注意，这里删除记录不需要模板文件，只需要删除了数据然后重定向到部门列表页面即可

![image-20260630124012983](./django的orm复习笔记.assets/image-20260630124012983.png)

#### 测试一下：我们可以先进入部门列表页面，这里每一行都有一个删除按钮，点击这个按钮就会把的确项的id作为查询字符串参数传递给删除页面，然后我们在后台获取这个id并且删除

![image-20260630123638976](./django的orm复习笔记.assets/image-20260630123638976.png)

#### 发现市场部被删除了，说明代码没有问题

![image-20260630124219661](./django的orm复习笔记.assets/image-20260630124219661.png)

## 3.8现在来实现修改功能

### 1》回到templates/dep_list.html，在修改超连接里面添加一个路径/dep/edit/?nid={{dep.id}}

![image-20260630124718556](./django的orm复习笔记.assets/image-20260630124718556.png)

### 2>然后我们在day47/ulrs.py里面添加一条路由dep/edit/,把它和day47app/views/dep_view.py里面的dep_edit函数（此时还没有创建）映射起来

![image-20260630124957388](./django的orm复习笔记.assets/image-20260630124957388.png)

### 3》然后我们需要在day47app/views/dep_view.py里面创建dep_edit函数，代码如下

![image-20260630125403268](./django的orm复习笔记.assets/image-20260630125403268.png)

### 4》然后我们需要在day47/templates里面创建一个dep_edit.html模板文件，内容如下

```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>编辑部门</title>
     <link rel="stylesheet" href="{% static 'plugins/bootstrap-3.4.1/css/bootstrap.min.css' %}">
    <style>
        .navbar{
            border-radius: 0;
        }
    </style>
</head>
<body>
<nav class="navbar navbar-default">
  <div class="container">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="#">用户管理系统</a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li><a href="/dep/list">部门管理</a></li>
        <li><a href="#">Link</a></li>
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="#">登录</a></li>
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">当前用户名称 <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="#">个人资料</a></li>
            <li><a href="#">我的信息</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">注销</a></li>
          </ul>
        </li>
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
<div>
    <div class="container">
        <div class="panel panel-default">
          <!-- Default panel contents -->
          <div class="panel-heading">
              <h3 class="panel-title">编辑部门</h3>
          </div>
          <div class="panel-body">
          {# 表单  #}
           <form action="/dep/edit/" method="post">
               {% csrf_token %}
              <div class="form-group">
                <label>部门名称</label>
                <div>
                  <input type="hidden" class="form-control" name="id"value="{{ dep.id }}">
                  <input type="text" class="form-control" name="title"value="{{ dep.title }}">
                </div>
              </div>
              <button type="submit" class="btn btn-success">更 新</button>
        </form>
          </div>
        </div>

    </div>
</div>


  <script src="{% static 'js/jquery3.7.1.min.js' %}"></script>
  <script src="{% static 'plugins/bootstrap-3.4.1/js/bootstrap.min.js' %}"></script>
</body>
</html>


```

#### 需要注意：编辑页面和新建页面有一个不一样的地方，就是编辑页面真正编辑的部门是由id的，所有我们需要创建一个隐藏字段，在这里保存我们获取到的id，在添加数据的时候需要把这个id一起提交

![image-20260630135751382](./django的orm复习笔记.assets/image-20260630135751382.png)

#### 测试一下，可以进入页面并且填充数据

![image-20260630135322637](./django的orm复习笔记.assets/image-20260630135322637.png)

#### 



### 5》回到dep_edit函数，添加堆post方法添加的数据的处理

![image-20260630135938651](./django的orm复习笔记.assets/image-20260630135938651.png)

#### 测试一下，把研发部改为人事部

![image-20260630140057636](./django的orm复习笔记.assets/image-20260630140057636.png)

#### 修改成功

![image-20260630140127316](./django的orm复习笔记.assets/image-20260630140127316.png)

### 注意：这里有几个个问题：

#### 1.员工表的部门信息是存部门名称还是部门id?

#### 存id

#### 2.部门id需要约束吗?

#### (应该是作为外键)它只能够是在部门表里面存在的id

#### 3.部门被删除了,和它关联的员工怎么处理?

#### 有2种处理方法

![image-20260630140723456](./django的orm复习笔记.assets/image-20260630140723456.png)

## 这里完成了创建项目并且初始化数据库和完成了dep/xxx/路由的所有处理其他模块我们会创建对应的笔记

