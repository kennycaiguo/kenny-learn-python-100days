from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.deprecation import MiddlewareMixin


class AuthMiddleware(MiddlewareMixin):
    """中间件1"""

    def process_request(self, req):
        # 0.有些页面不需要先登录才能访问的,如登录页面,这些页面需要直接让他通过比如login页面,利用request对象的path_info来实现
        # 这一步操作非常关键,如果没有这一步,你永远无法登录成功
        if req.path_info in ['/login/','/image/code/']:
            return
        # 1.读取当前用户的session信息,如果有信息,说明登录了,可以继续往后走
        info = req.session.get("info")
        if info:
            return
        # 2.没有登录,重定向到登录页面
        return redirect("/login/")






