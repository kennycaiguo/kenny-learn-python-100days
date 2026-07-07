"""
URL configuration for vote project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 注册用户
    path('register/',views.register,name='register'),
    # 登录
    path('login/',views.login,name="login"),
    path('captcha/',views.get_captcha,name='get_captcha'),
    path('',views.show_subjects,name="show_subjects"),
    # path('teachers/',views.show_teachers,name="show_teachers"),
    path('teachers/query/',views.get_teachers,name="get_teachers"),
    # gcount
    path('praise/',views.good_or_bad,name="good_count"),
    path('scold/',views.good_or_bad,name="bad_count"),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register'),
    path('excel/', views.export_teachers_excel),
    path('teachers_data/', views.get_teachers_data,name='get_teachers_data'),
    path('teacher_stat/',views.teacher_stat,name="teacher_stat"),
    path('setcache/',views.set_subject_cache,name='set_subject_cache'),
    # api/xxx/路由
    # path('api/subjects/',views.show_objects_api,name='show_objects_api')
    # path('api/subjects/',views.show_objects_api2,name='show_objects_api2'),
    # path('api/subjects/',views.SubjectView.as_view(),name='SubjectView'),
    # path('api/subjects/',views.show_subjects_api_cache,name='show_subjects_api_cache'),
    path('api/subjects/', views.show_subjects_redis, name='show_subjects_redis'),
    path('api/teachers/query/', views.get_teachers_api,name='show_teachers_api'),
]
