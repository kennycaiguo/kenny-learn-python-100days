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
    path('',views.show_subjects,name="show_subjects"),
    path('teachers/',views.show_teachers,name="show_teachers"),
    path('teachers/query/',views.get_teachers,name="get_teachers"),
    # gcount
    path('praise/',views.good_or_bad,name="good_count"),
    path('scode/',views.good_or_bad,name="bad_count"),
]
