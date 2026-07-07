"""
URL configuration for mysite project.

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
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from mySiteApp import views




urlpatterns = [
    # path('admin/', admin.site.urls),
    path(r'', views.home),
    path('index/', views.index),
    path('reg/', views.register),
    path('userlist/', views.user_list),
    path('tpl/', views.tpl),
    path('movies/', views.movies),
    path('req_test/', views.reqTest),
    path('login/', views.login),
    path('orm/', views.orm),
    # path('users/', views.showAll),
    path('info/list/', views.showAll),  #添加这两个路由是为了更加规范我们的路由写法
    # path('add/', views.addNew),
    path('info/add/', views.addNew),   #添加这两个路由是为了更加规范我们的路由写法
    path('info/delete/', views.deleteOne),   #规范我们的路由写法
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
