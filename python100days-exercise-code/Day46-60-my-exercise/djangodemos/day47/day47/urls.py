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


from day47app.views import dep_view,user_view

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
    path('user/list/',user_view.user_list,name="user_list")
]
