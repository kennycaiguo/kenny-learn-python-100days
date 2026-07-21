from pyecharts.charts import Bar,Pie,Map
from pyecharts import options as opts

# 创建柱状图对象并设置初始参数（宽度、高度）
# bar_chart = Bar(init_opts=opts.InitOpts(width='600px', height='450px'))
# # 设置横轴数据
# bar_chart.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# # 设置纵轴数据（第一组）
# bar_chart.add_yaxis("商家A", [25, 20, 36, 10, 75, 90])
# # 设置纵轴数据（第二组）
# bar_chart.add_yaxis("商家B", [15, 12, 30, 20, 45, 60])
# # 设置纵轴数据（第三组）
# bar_chart.add_yaxis("商家C", [12, 32, 40, 52, 35, 26])
# # 添加全局配置参数
# bar_chart.set_global_opts(
#     # 横轴相关的参数
#     xaxis_opts=opts.AxisOpts(
#           axislabel_opts=opts.LabelOpts(color='navy'),
#            # 纵轴相关的参数（标签、最小值、最大值、间隔）
#     ),
#     yaxis_opts=opts.AxisOpts(
#         axislabel_opts=opts.LabelOpts(color='navy'),
#         min_=0,
#         max_=100,
#         interval=10
#        ),
#     # 标题相关的参数（内容、链接、位置、文本样式）
#     title_opts=opts.TitleOpts(
#         title='2022年销售数据展示',
#         pos_left='2%',
#         title_textstyle_opts=opts.TextStyleOpts(
#             color='navy',
#             font_size=16,
#             font_family='苹方-简',
#             font_weight='bold'
#         )
#     ),
#     # 工具箱相关的参数
#     toolbox_opts=opts.ToolboxOpts(
#         orient='vertical',
#         pos_left='right'
#     )
 

# )

# bar_chart.load_javascript()
# bar_chart.render("sales_chart.html")

# pyecharts绘制饼图
# 准备饼图需要的数据
# x_data = ["直接访问", "邮件营销", "联盟广告", "视频广告", "搜索引擎"]
# y_data = [335, 310, 234, 135, 1548]
# data = [(x, y) for x, y in zip(x_data, y_data)]

# # 创建饼图对象并设置初始化参数
# pie_chart = Pie(init_opts=opts.InitOpts(width="800px", height="400px"))
# # 向饼图添加数据
# pie_chart.add(
#     '', 
#     data_pair=data,
#     radius=["50%", "75%"],
#     label_opts=opts.LabelOpts(is_show=False),
# )
# # 设置全局配置项
# pie_chart.set_global_opts(
#     # 配置图例相关的参数
#     legend_opts=opts.LegendOpts(
#         pos_left="legft",
#         orient="vertical"
#     )
# )
# # 设置数据系列配置参数
# pie_chart.set_series_opts(
#     # 设置不显示工具提示
#     tooltip_opts=opts.TooltipOpts(is_show=False),
#     # 设置饼图标签的样式
#     label_opts=opts.LabelOpts(formatter="{b}({c}): {d}%")
# )
# pie_chart.load_javascript()
# pie_chart.render("baidu_pie.html")

# 最后，我们来看看如何绘制地图，绘制地图首先需要安装额外的依赖库来获取地图相关信息，命令如下所示。
#  不能直接安装，需要下载对应的库然后用：python setup.py install安装
data = [
    ('广东', 594), ('浙江', 438), ('四川', 316), ('北京', 269), ('山东', 248),
    ('江苏', 234), ('湖南', 196), ('福建', 166), ('河南', 153), ('辽宁', 152),
    ('上海', 138), ('河北', 86), ('安徽', 79), ('湖北', 75), ('黑龙江', 70), 
    ('陕西', 63), ('吉林', 59), ('江西', 56), ('重庆', 46), ('贵州', 39),
    ('山西', 37), ('云南', 33), ('广西', 24), ('天津', 22), ('新疆', 21),
    ('海南', 18), ('内蒙古', 14), ('台湾', 11), ('甘肃', 7), ('广西壮族自治区', 4),
    ('香港', 4), ('青海', 3), ('新疆维吾尔自治区', 3), ('内蒙古自治区', 3), ('宁夏', 1)
]

map_chart = Map(init_opts=opts.InitOpts(width='1000px', height='1000px'))
map_chart.add('', data, 'china', is_roam=False)
map_chart.load_javascript()
map_chart.render("china_map.html")