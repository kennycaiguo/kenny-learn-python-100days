from django.shortcuts import render, redirect
from django.http import HttpResponse
from mySiteApp import models


# Create your views here.
def index(request):
    print(request)
    return HttpResponse("Welcome to index of mysite...")


def home(req):
    print(req)
    return HttpResponse('<h1>This is the home page</h1>')


def user_list(req):
    return render(req, "userlist.html")


def register(req):
    return render(req, "register.html")


def tpl(req):
    jobs = ["管理员", "司机", "保安"]
    isGood = True
    jack = {
        "name": "Jack",
        "age": 19,
        "gender": "male"
    }
    users = [
        {"id": "u001", "name": "Mary", "gender": "Female", "age": 20},
        {"id": "u002", "name": "Ron", "gender": "Male", "age": 21},
        {"id": "u003", "name": "Magret", "gender": "Female", "age": 22},
    ]
    return render(req, "tpl.html",
                  {
                      'msg': "Hello Django Template!!!",
                      'jobs': jobs,
                      "state": isGood,
                      "person": jack,
                      "users": users
                  })


def movies(req):
    import requests
    from bs4 import BeautifulSoup

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    }
    url = "https://movie.douban.com/top250"
    # 这里只是爬取一页
    sub_url = url + f"?start=0"
    res = reps = requests.get(sub_url, headers=headers).text
    # print(reps.text)

    soup = BeautifulSoup(res, "html.parser")
    # print(soup)

    titles = soup.findAll("span", attrs={"class": "title"})
    bds = soup.findAll("div", attrs={"class": "bd"})
    chinese_titles = []
    summ = []
    for bd in bds:
        # print(bd.p.text)
        summ.append(bd.p.text)
    for title in titles:
        # print(title.string) # 不要标签,只需要标签里面的内容
        # if not title.string.__contains__("/"):  # 过滤掉英文标题,注意到英文标题都是以 / 开头  ok
        # if title.string.find("/")==-1:  # 过滤掉英文标题,注意到英文标题都是以 / 开头  ok,find方法找到了返回一个不是负数的结果,-1表示找不到,我们这里就需要它找不到
        if "/" not in title.string:  # 过滤掉英文标题,注意到英文标题都是以 / 开头 也是ok的
            chinese_titles.append(title.string)
            # print(title.string)
    summ.pop(0)
    # print(summ)
    # print(chinese_titles)
    movies = dict(zip(chinese_titles, summ))
    print(movies)
    return render(req, "movies.html", {"movies": movies})


def reqTest(req):
    print(req)
    # 获取请求方式
    print(req.method)
    print(req.body)  # post请求发送过来的数据 # 这里是空,因为这是get请求
    print(req.user)  # AnonymousUser
    print(req.headers)
    print(req.session)
    print(req.path)
    print(req.META)
    print(req.GET)  # 可以获取get请求参数
    print(req.POST)  # 可以获取post请求数据

    # return HttpResponse("服务器返回的数据")
    return redirect("/userlist")


def login(req):
    if req.method == "GET":
        return render(req, "login.html")
    # post请求,需要获取用户信息
    print(req.POST)
    # 数据校验
    user = req.POST.get("username")
    pwd = req.POST.get("password")
    if user == "root" and pwd == "root":
        # return HttpResponse("登录成功")
        return redirect("/index/")
    return render(req, "login.html", {"error": "用户名或者密码错误"})


def orm(req):
    """1.新增"""
    # models.Department.objects.create(title="销售部")
    # models.Department.objects.create(title="IT部")
    # models.Department.objects.create(title="运营部")

    # 用户信息表
    # models.UserInfo.objects.create(name="Jack",password="1234",age=18)
    # models.UserInfo.objects.create(name="Kitty",password="123",age=19)
    # models.UserInfo.objects.create(name="Mimi",password="234",age=17)

    """2.删除"""
    # 删除数据,需要先筛选数据,选出来后再删除
    # models.UserInfo.objects.filter(id=3).delete() # 删除id为3的一行数据
    # models.Department.objects.all().delete() # 删除部门表的全部数据

    """3.查询(筛选)"""
    # 3.1查询所有,返回一个QuerySet,是一个列表一样的东西,可以遍历
    # for item in models.UserInfo.objects.all():
    #     print(item.id,item.name,item.password,item.age)
    # 3.2查询一条数据
    # data = models.UserInfo.objects.filter(id=1) #即使只有一条数据,它还是一个列表
    # for user in data:
    #     print(user.id,user.name,user.password,user.age)
    # 3.3 如果你非常确定只有一条数据,你可以这么写
    # user = models.UserInfo.objects.filter(id=1).first()
    # print(user.id,user.name,user.password,user.age)
    """4.更新数据"""
    # 4.1更新所有数据
    # models.UserInfo.objects.all().update(password="888")
    # 4.2更新某一些或者某一个数据
    models.UserInfo.objects.filter(id=2).update(password="6666")
    return HttpResponse("操作成功")


def showAll(req):
    users = models.UserInfo.objects.all()
    return render(req, "all.html", {'users': users})


def addNew(req):
    if req.method == "GET":
        return render(req, "add_new.html")
    # post请求
    # username = req.POST.get("")
    # print(req.POST)
    username = req.POST.get("username")
    password = req.POST.get("password")
    age = req.POST.get("age")
    models.UserInfo.objects.create(name=username, password=password, age=age)
    # return HttpResponse("添加新用户成功")
    return redirect("/info/list")

def deleteOne(req):
    nid = req.GET.get("nid")
    models.UserInfo.objects.filter(id=nid).delete()
    # 重定向到/info/list
    return redirect("/info/list")