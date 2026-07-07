from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from day16 import settings
from day16app import views
from day16app.views import dep_view,user_view,pretty_view,home_view,admin_view,acc_view,task_view

urlpatterns = [
          # path('admin/', admin.site.urls),
          path('', home_view.home),
          path('index/', home_view.index),
          # 部门管理相关路由
          path('dep/list/', dep_view.dep_list),
          path('dep/add/', dep_view.dep_add),
          path('dep/del/', dep_view.dep_del),
          # 路由格式 :http://127.0.0.1:8000/dep/1/edit
          path('dep/<int:nid>/edit/', dep_view.dep_edit),

          # 员工管理相关路由
          path('user/list/', user_view.user_list),
          path('user/add/', user_view.user_add),
          path('user/<int:nid>/edit/', user_view.user_edit),
          path('user/<int:nid>/del/', user_view.user_del),

          # 靓号管理相关路由
          path('pretty/list/', pretty_view.pretty_list),
          #添加靓号
          path('pretty/add/', pretty_view.pretty_add),
          #修改靓号
          path('pretty/<int:nid>/edit/', pretty_view.pretty_edit),
          # 删除靓号
          path('pretty/<int:nid>/del/', pretty_view.pretty_del),
          #管理员账户管理
          #管理员列表
          path('admin/list/',admin_view.admin_list),
          # 新增管理员
          path('admin/add/',admin_view.admin_add),
          # 编辑管理员信息
          path('admin/<int:nid>/edit/',admin_view.admin_edit),
          # 重置管理员密码
          path('admin/<int:nid>/reset/',admin_view.admin_reset),
          # 删除管理员
          path('admin/<int:nid>/del/',admin_view.admin_del),

          #登录相关路由
          path('login/',acc_view.login),
          # 注销或者说退出登录
          path('logout/',acc_view.logout),
          # 动态生成验证码的路由
          path("image/code/",acc_view.image_code),

          # ajax测试任务管理
          path("task/test/list",task_view.task_test_list),
          path("task/test/ajax/",task_view.task_test_ajax),
          # ajax 请求发送表单数据
          path("task/test/ajax2/",task_view.task_test_ajax2),

          # 任务管理
          path("task/list/",task_view.task_list),
          path("task/add/",task_view.task_add),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
