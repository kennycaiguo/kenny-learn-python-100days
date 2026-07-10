import json
from pipes import quote

import xlwt
from django.shortcuts import render, redirect
from django_redis import get_redis_connection

from polls.models import Subject, Teacher, User
from django.http import JsonResponse, HttpResponse
from polls.utils import *
from vote.middlewares import check_login_middleware
from bpmappers.djangomodel import ModelMapper
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class SubjectMapper(ModelMapper):
    class Meta:
        model = Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class SubjectSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('no', 'name')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        exclude = ('subject',)


# Create your views here.
def show_subjects(request):
    subjects = Subject.objects.all().order_by('no')
    return render(request, 'subjects.html', {'subjects': subjects})


def show_objects_api(request):
    res = Subject.objects.all().order_by('no')
    subjects = []
    for s in res:
        subjects.append(SubjectMapper(s).as_dict())
    return JsonResponse(subjects, safe=False)


@api_view(('GET',))
def show_objects_api2(request):
    subjects = Subject.objects.all().order_by('no')
    # 创建序列化器对象并指定要序列化的模型
    # serializer = SubjectSerializer(subjects, many=True)
    serializer = SubjectSimpleSerializer(subjects, many=True)
    # 通过序列化器的data属性获得模型对应的字典并通过创建Response对象返回JSON格式的数据
    return Response(serializer.data)


## 这个类可以代替上面两个api函数,注意，这个类一定要有一个queryset属性，否则报错
@method_decorator(decorator=cache_page(timeout=86400, cache='default'), name='get')
class SubjectView(ListAPIView):
    queryset = Subject.objects.all().order_by('no')
    serializer_class = SubjectSerializer


@api_view(('GET',))
@cache_page(timeout=86400, cache='default')
def show_subjects_api_cache(request):
    queryset = Subject.objects.all().order_by('no')
    data = SubjectSerializer(queryset, many=True).data
    return Response({'code': 20000, 'subjects': data})


def set_subject_cache(request):
    redis_cli = get_redis_connection()
    # 如果缓存中没有获取到学科数据就查询数据库
    queryset = Subject.objects.all()
    data = SubjectSerializer(queryset, many=True).data
    # 将查到的学科数据序列化后放到缓存中
    # redis_cli.set('vote:polls:subjects', json.dumps(data), ex=86400)
    redis_cli.set('vote_polls_subjects', json.dumps(data), ex=86400)
    return HttpResponse("Redis Cache Has Been successfully...")


@api_view(['GET'])
def show_subjects_redis(request):
    """获取学科数据"""
    redis_cli = get_redis_connection()
    # 先尝试从缓存中获取学科数据
    data = redis_cli.get('vote_polls_subjects')
    if data:
        # 如果获取到学科数据就进行反序列化操作
        data = json.loads(data)
    else:
        # 如果缓存中没有获取到学科数据就查询数据库
        queryset = Subject.objects.all()
        data = SubjectSerializer(queryset, many=True).data
        # 将查到的学科数据序列化后放到缓存中
        redis_cli.set('vote_polls_subjects', json.dumps(data), ex=86400)
    return Response({'code': 20000, 'subjects': data})


def show_teachers(request):
    teachers = Teacher.objects.all()
    return None


@api_view(('GET',))
def get_teachers_api(request):
    try:
        sno = int(request.GET.get('sno'))
        subject = Subject.objects.only('name').get(no=sno)
        teachers = Teacher.objects.filter(subject=subject).defer('subject').order_by('no')
        subject_seri = SubjectSimpleSerializer(subject)
        teacher_seri = TeacherSerializer(teachers, many=True)
        return Response({'subject': subject_seri.data, 'teachers': teacher_seri.data})
    except (TypeError, ValueError, Subject.DoesNotExist):
        return Response(status=404)


def get_teachers(request):
    try:
        sno = int(request.GET.get('sno'))
        teachers = []
        if sno:
            subject = Subject.objects.only('name').get(no=sno)
            teachers = Teacher.objects.filter(subject=subject).order_by('no')
        return render(request, 'teacher.html', {
            'subject': subject,
            'teachers': teachers
        })
    except (ValueError, Subject.DoesNotExist):
        return redirect('/')


# /praise/?tno=1 gcount
# /scold/?tno=2  bcount
def good_or_bad(request):
    if request.session.get('userid'):
        try:
            tno = int(request.GET.get('tno'))
            teacher = Teacher.objects.get(no=tno)
            if request.path.startswith('/praise'):
                teacher.gcount += 1
                count = teacher.gcount
            else:
                teacher.bcount += 1
                count = teacher.bcount
            teacher.save()
            data = {
                "code": 20000, "msg": "投票成功", "count": count
            }
        except (ValueError, Teacher.DoesNotExist):
            data = {
                "code": 20002, "msg": "投票失败"
            }
    else:
        data = {
            "code": 20001, "msg": "请先登录"
        }
    return JsonResponse(data)


def login(request):  # 为了方便学习，我们所有用户的密码都设置为12345
    hint = ''
    if request.method == 'GET':
        return render(request, 'login.html')
    # post 请求
    username = request.POST.get("username")
    password = request.POST.get("password")
    captcha = request.POST.get('captcha')
    print(captcha, captcha == request.session.get('captcha'))
    if username and password:
        password = gen_hash_digest(password)
        user = User.objects.filter(username=username, password=password).first()
        # print(user.username)
        # if user exists,means the above 2 are correct
        if user:
            request.session['userid'] = user.no
            request.session['username'] = user.username
            # redirect to home
            return redirect('/')
        else:  # user doesn't exists
            hint = '用户名或者密码错误'
    else:
        hint = '请输入有效的用户名和密码'
    return render(request, 'login.html', {"hint": hint})


def get_captcha(request):
    captcha_text = gen_random_code()
    request.session['captcha'] = captcha_text
    print(captcha_text)
    img_data = Captcha.instance().generate(captcha_text)
    return HttpResponse(img_data, content_type='image/png')


def export_teachers_excel(request):
    # 创建工作簿
    wb = xlwt.Workbook()
    # 添加工作表
    sheet = wb.add_sheet('老师信息表')
    # 查询所有老师的信息
    queryset = Teacher.objects.all()
    # 向Excel表单中写入表头
    colnames = ('姓名', '介绍', '好评数', '差评数', '学科')
    for index, name in enumerate(colnames):
        sheet.write(0, index, name)
    # 向单元格中写入老师的数据
    props = ('name', 'intro', 'gcount', 'bcount', 'subject')
    for row, teacher in enumerate(queryset):
        for col, prop in enumerate(props):
            value = getattr(teacher, prop, '')
            if isinstance(value, Subject):
                value = value.name
            sheet.write(row + 1, col, value)
    # 保存Excel
    buffer = BytesIO()
    wb.save(buffer)
    # 将二进制数据写入响应的消息体中并设置MIME类型
    resp = HttpResponse(buffer.getvalue(), content_type='application/vnd.ms-excel')
    # 中文文件名需要处理成百分号编码
    filename = quote('老师.xls')
    # 通过响应头告知浏览器下载该文件以及对应的文件名
    resp['content-disposition'] = f'attachment; filename*=utf-8\'\'{filename}'
    return resp


def logout(request):
    request.session.flush()
    return redirect('/login')


def register(request):  # 注意:为了方便编程，我们把所有用户的密码都设置为12345
    hint = ''
    # get请求
    if request.method == 'GET':
        return render(request, 'register.html')
    # post请求
    username = request.POST.get("username")
    password = request.POST.get("password")
    retype = request.POST.get("retype_pw")
    tel = request.POST.get("tel")
    if password == retype:  # 两次输入的密码必须一致
        # 需要先查询一下数据库有没有这个用户，如果已经存在，不允许创建相同名称的用户
        user = User.objects.filter(username=username)
        if user:
            hint = '该用户已经存在'
            return render(request, "register.html", {"hint": hint})
        else:
            password = gen_hash_digest(password)
            User.objects.create(username=username, password=password, tel=tel)
            return redirect('/login/')
    return render(request, "register.html", {"hint": "两次输入的密码不一样"})


def teacher_stat(request):
    return render(request, 'teacher_stat.html')


def get_teachers_data(request):
    queryset = Teacher.objects.all()
    names = [teacher.name for teacher in queryset]
    good_counts = [teacher.gcount for teacher in queryset]
    bad_counts = [teacher.bcount for teacher in queryset]
    return JsonResponse({'names': names, 'good': good_counts, 'bad': bad_counts})
