"""
URL configuration for day47 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from django.shortcuts import render


from day47app.views import dep_view, pretty_view,user_view,admin_view

def index(request):
    return render(request, 'index.html')
urlpatterns = [
    #    path('admin/', admin.site.urls),
    path('',dep_view.home,name='index'),
    # department urls
    path("dep/",dep_view.dep_home,name="dep_home"),
    path("dep/list/",dep_view.dep_list,name="dep_list"),
    path('dep/add/',dep_view.dep_add,name="dep_add"),
    path('dep/del/',dep_view.dep_del,name="dep_del"),
    # path('dep/edit/',dep_view.dep_edit,name="dep_edit"),
    path('dep/<int:nid>/edit/',dep_view.dep_edit,name="dep_edit"),
    # users urls
    path('user/list/',user_view.user_list,name="user_list"),
    path('user/add/',user_view.user_add,name='user_add'),
    path('user/<int:nid>/edit/',user_view.user_edit,name='user_edit'),
    path('user/del/',user_view.user_del,name='user_del'),
    # pretty number route
    path('pretty/list/',pretty_view.pretty_list,name='pretty_list'),
    path('pretty/add/',pretty_view.pretty_add,name='pretty_add'),
    path('pretty/<int:nid>/edit/',pretty_view.pretty_edit,name='pretty_edit'),
    path('pretty/<int:nid>/del/',pretty_view.pretty_del,name='pretty_del'),
    # admin routes
    path("admin/list/",admin_view.admin_list,name='admin_list'),
    path("admin/add/",admin_view.admin_add,name="admin_add"),
    path("admin/<int:nid>/edit/",admin_view.admin_edit,name="admin_edit"),
    path("admin/<int:nid>/del/",admin_view.admin_del,name="admin_del"),
    path("admin/<int:nid>/reset/",admin_view.admin_reset,name='admin_reset')
]
