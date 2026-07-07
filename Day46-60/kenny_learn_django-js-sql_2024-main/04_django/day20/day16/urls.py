from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from django.views.static import serve

from day16 import settings
from day16app import views
from day16app.views import dep_view,user_view,pretty_view,home_view,admin_view,acc_view,task_view,order_view,chart_view,upload_view,city_view

urlpatterns = [
          # path('admin/', admin.site.urls),
          # 注意:这个serve函数,在很多包里面都有,这里需要django.views.static.serve
          re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT},name='media'),
          path('', home_view.home),
          path('index/', home_view.index),
          # 部门管理相关路由
          path('dep/list/', dep_view.dep_list),
          path('dep/add/', dep_view.dep_add),
          path('dep/del/', dep_view.dep_del),
          # 路由格式 :http://127.0.0.1:8000/dep/1/edit
          path('dep/<int:nid>/edit/', dep_view.dep_edit),
          # 处理excel文件上传,然后把他的数据添加到数据库中
          path("dep/multiadd/",dep_view.dep_multiadd),

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
          # 订单管理
          path("order/list/",order_view.order_list),
          path("order/add/",order_view.order_add),
          path("order/del/",order_view.order_del),
          # 处理Ajax查询请求
          path("order/detail/",order_view.order_detail),
          path("order/<int:eId>/edit/",order_view.order_edit),
          path("order/edit2/",order_view.order_edit2),

          # 图表
          path("chart/list",chart_view.chart_list),
          # 处理柱状图的请求
          path("chart/bar/",chart_view.chart_bar),
          # 处理饼状图请求
          path("chart/pie/",chart_view.chart_pie),
          # 处理这些图请求
          path("chart/line/",chart_view.chart_line),

          # 文件上传相关路由,改为用ModelForm上传
          path("upload/list/",upload_view.upload_list),
          # 路由django的Form组件来实现上传功能
          path("upload/form/",upload_view.upload_form),
          # 使用ModelForm上传的便捷方式
          path("upload/modelform/",upload_view.upload_model_form),

          # 城市列表
          path("city/list/",city_view.city_list),
          # 新增城市
          path("city/add/",city_view.city_add),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
