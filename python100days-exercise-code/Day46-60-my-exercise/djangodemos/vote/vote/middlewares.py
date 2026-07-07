from django.http import JsonResponse
from django.shortcuts import redirect

# 需要登录才能访问的资源路径
LOGIN_REQUIRED_URLS = {'/praise/', '/scold/', '/excel/', '/teachers_data/','/teacher_stat/','/teachers/query/'}


def check_login_middleware(get_resp):
    def wrapper(request, *args, **kwargs):
        # 路径是否在上面的集合中
        if request.path in LOGIN_REQUIRED_URLS:
            # 如果是，就判断是否有userid，如果有才是以及登录了
            if 'userid' not in request.session:
                # 如果没有登录，判断是否是ajax请求
                # if request.is_ajax(): # 过时了，django4.0以上这个函数以及移除
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    # 如果是ajax请求，就返回一个json提示用户登录
                    return JsonResponse({"code": 10001, "msg": "请先登录"})
                else:
                    # 如果不是ajax请求，我们就重定向到/login/
                    back_url = request.get_full_path()
                    # 非Ajax请求直接重定向到登录页
                    return redirect(f'/login/?back_url={back_url}')
        # 调用被装饰的函数
        return get_resp(request, *args, **kwargs)

    return wrapper
