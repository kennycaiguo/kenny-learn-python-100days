"""
自己封装的分页类
使用方法:
原来的数据
   term = {}
    kw = req.GET.get("kw", "")
    if kw:
        term["mobile__contains"] = kw

    pretty_data = models.PrettyNumber.objects.filter(**term).order_by("-level")
1.实例化分页组件对象
    pretty_data = models.PrettyNumber.objects.filter(**term).order_by("-level")
    page_obj = Pagination(req,pretty_data)
2.获取分页后数据
     page_query_set = page_obj.page_queryset
3.获取分页组件的html字符串,可以直接显示在页面说
     page_str = page_obj.gen_html()
4.渲染数据
     return render(req, "pretty_list.html", {"pretties": page_query_set, "kw": kw, "page_str": page_str})
"""
from django.utils.safestring import mark_safe
import copy

class Pagination(object):
    def __init__(self,request,queryset, page_size=10, page_param="page", incr=5):
        """
        参数说明
        :param request:        请求对象,用来获取查询字符串参数
        :param queryset:       符合添加的查询数据,用来做计算分页相关数据
        :param page_size:      每一页显示多少条数据
        :param page_param:     查询参数
        :param incr:           需要显示的前和后的条数的增量
        """
        query_dict = copy.deepcopy(request.GET)  # 获取请求中的GET对象并且做一个深拷贝
        query_dict._mutable = True   #把拷贝的可修改属性设置为真
        self.query_dict = query_dict  # 保存这个拷贝,方便以后使用
        self.page_param = page_param

        page = request.GET.get(page_param, "1")  # 默认是第一页
        # 保证page是数字字符串
        if page.isdecimal():
            page = int(page)  # 转化为整数
        else:  # 如果我们获取到的参数不是数字字符,就把page设置为1
            page = 1
        self.page = page
        self.page_size = page_size
        self.start = (page - 1) * page_size  # 计算开位置
        self.end = page * page_size
        self.page_queryset = queryset[self.start:self.end]
        count = queryset.count()
        # 计算总页数
        page_count, remain = divmod(count, page_size)  # divmod(a,b)函数会计算 a/b然后返回一个元组(商,余数),我们可以用2个变量来接受,一个是商,另外一个是余数
        if remain:
            page_count += 1  # 如果余数不为0,总页数需要+1,即使余数是1也需要+1
        self.total_page_count = page_count
        self.incr = incr

    def gen_html(self):
        # incr = 5
        if self.total_page_count <= 2 * self.incr + 1:  # 数据库的数据比较少的时候
            page_start = 1
            page_end = self.total_page_count
        else:
            # 数据库的数据比较多
            if self.page <= self.incr:  # 当前页码比增量还小或者等于增量,就把起始页码固定为1
                page_start = 1
                page_end = 2 * self.incr + 1
            else:
                if (self.page + 5) > self.total_page_count:
                    page_start = self.total_page_count - 2 * self.incr
                    page_end = self.total_page_count
                else:
                    page_start = self.page - self.incr
                    page_end = self.page + self.incr

        page_str_list = []
        self.query_dict.setlist(self.page_param,[1])

        # 首页
        first = '<li><a href="?{}">首页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(first)
        # 上一页
        if self.page > 1:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(prev)

        for i in range(page_start, page_end + 1):  # 这里page_count需要加1因为for...range不包括后面的值
            self.query_dict.setlist(self.page_param, [i])
            if i == self.page:
                el = '<li class="active"><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)  # 如果是当前页面,我们给他添加一个样式
            else:
                el = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_str_list.append(el)
            # page_str = mark_safe("".join(page_str_list))

        # 下一页
        if self.page >= self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.total_page_count])
            next = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [self.page + 1])
            next = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(next)

        # 尾页
        self.query_dict.setlist(self.page_param, [self.total_page_count])
        last = '<li><a href="?{}">尾页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(last)

        search_str = """
                     <li>
                         <form style="float: left;margin-left: -1px;" method="get">
                              <input type="text" name="page"
                                     style="position: relative; float: left;display: inline-block;width: 80px;"
                                     class="form-control"
                                     placeholder="输入页码...">

                              <button class="btn btn-default" type="submit">跳转</button>
                         </form>
                     </li>
            """

        page_str_list.append(search_str)
        page_str = mark_safe("".join(page_str_list))
        return page_str
