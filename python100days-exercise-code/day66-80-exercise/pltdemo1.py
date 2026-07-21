import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'].insert(0, 'SimHei')
plt.rcParams['axes.unicode_minus'] = False
# plt.figure(figsize=(8,4),dpi=120,facecolor='darkgray')
# plt.subplot(2, 2, 1)

# x = np.linspace(-2*np.pi,2*np.pi,120)
# y = np.sin(x)

# 创建画布
# plt.figure(figsize=(8, 4), dpi=120)
# plt.plot(x,y,linewidth=2,marker='^',color='green')
# plt.show()

x = np.linspace(-2*np.pi,2*np.pi,120)
sin_x,cos_x = np.sin(x),np.cos(x)
# one canvas
# plt.plot(x,sin_x,linewidth=2,marker='*',color='green')
# plt.plot(x,cos_x,linewidth=2,marker='D',color='cyan')
# 2 rows
# plt.subplot(2,1,1)
# plt.plot(x,sin_x,linewidth=2,marker='*',color='deeppink')
# plt.subplot(2,1,2)
# plt.plot(x,cos_x,linewidth=2,marker='D',color='cyan')
# 2 columns
# plt.subplot(1,2,1)
# plt.plot(x,sin_x,linewidth=2,marker='*',color='deeppink')
# plt.subplot(1,2,2)
# plt.plot(x,cos_x,linewidth=2,marker='D',color='cyan')

# fig.add_axes
# fig = plt.figure(figsize=(10,4),dpi=120,facecolor='darkgray')
# plt.plot(x,sin_x,linewidth=2,marker='*',color='deeppink')
# ax = fig.add_axes((0.695, 0.6, 0.3,0.25))
# ax.plot(x,cos_x,linewidth=2,marker='D',color='cyan')
# ax = fig.add_axes((0, 0.2, 0.3,0.25))
# ax.plot(x,cos_x,linewidth=2,marker='o',color='yellow')
# plt.show()

# 散点图
# x = np.array([5550, 7500, 10500, 15000, 20000, 25000, 30000, 40000])
# y = np.array([800, 1800, 1250, 2000, 1800, 2100, 2500, 3500])

# plt.figure(figsize=(6,4),dpi=120)
# plt.scatter(x,y)
# plt.show()

#### 柱状图

# 在对比数据的差异时，柱状图是非常棒的选择，我们可以使用`pyplot`模块的`bar`函数来生成柱状图，也可以使用`barh`函数来生成水平柱状图（也称为“条状图”）。
# 我们先为柱状图准备一些数据，代码如下所示。
x=np.arange(4)
y1 = np.random.randint(20,50,4)
y2 = np.random.randint(25,60,4)

# plt.figure(figsize=(6,4),dpi=120)
# plt.bar(x-0.1,y1, width=0.2, label='销售A组')
# plt.bar(x+0.1,y2, width=0.2, label='销售B组')
# 定制横轴的刻度
# plt.xticks(x, labels=['Q1', 'Q2', 'Q3', 'Q4'])
# plt.legend()
# plt.show()

# 堆叠柱状图
# labels = ['Q1', 'Q2', 'Q3', 'Q4']
# plt.bar(labels, y1, width=0.4, label='销售A组')
# # 注意：堆叠柱状图的关键是将之前的柱子作为新柱子的底部，可以通过bottom参数指定底部数据，新柱子绘制在底部数据之上
# plt.bar(labels, y2, width=0.4, bottom=y1, label='销售B组')
# plt.legend(loc='lower right')
# plt.show()

#### 饼状图

# 饼状图通常简称为饼图，是一个将数据划分为几个扇形区域的统计图表，它主要用于描述数量、频率等之间的相对关系。在饼图中，每个扇形区域的大小就是其所表示的数量的比例，
# 这些扇形区域合在一起刚好是一个完整的饼。在需要展示数据构成的场景下，饼状图、树状图和瀑布图是不错的选择，我们可以使用`pyplot`模块的`pie`函数来绘制饼图
data = np.random.randint(100, 500, 7)
labels = ['苹果', '香蕉', '桃子', '荔枝', '石榴', '山竹', '榴莲']

# plt.figure(figsize=(5,5),dpi=120)
# plt.pie(
#     data,
#     # 自动显示百分比
#     autopct='%.1f%%',
#     radius=1,
#     # 百分比到圆心的距离
#     pctdistance=0.8,
#       # 颜色（随机生成）
#     colors=np.random.rand(7, 3),
#     # 字体属性
#     textprops=dict(fontsize=8, color='black'),
#     # 楔子属性（生成环状饼图的关键）
#     wedgeprops=dict(linewidth=1, width=1), # width参数控制每一块饼的楔子的面积大小
#     # 标签
#     labels=labels
# )

# plt.show()

#### 直方图

# 在统计学中，直方图是一种展示数据分布情况的图形，是一种二维统计图表，它的两个坐标分别是统计样本和该样本对应的某个属性的度量。
# 下面的数据是某学校100名男学生的身高，如果我们想知道数据的分布，就可以使用直方图。
heights = np.array([
    170, 163, 174, 164, 159, 168, 165, 171, 171, 167, 
    165, 161, 175, 170, 174, 170, 174, 170, 173, 173, 
    167, 169, 173, 153, 165, 169, 158, 166, 164, 173, 
    162, 171, 173, 171, 165, 152, 163, 170, 171, 163, 
    165, 166, 155, 155, 171, 161, 167, 172, 164, 155, 
    168, 171, 173, 169, 165, 162, 168, 177, 174, 178, 
    161, 180, 155, 155, 166, 175, 159, 169, 165, 174, 
    175, 160, 152, 168, 164, 175, 168, 183, 166, 166, 
    182, 174, 167, 168, 176, 170, 169, 173, 177, 168, 
    172, 159, 173, 185, 161, 170, 170, 184, 171, 172
])

# plt.figure(figsize=(8,4),dpi=120)
# # 绘制直方图
# # plt.hist(heights,bins=np.arange(145,196,5),color='deeppink')
# # 绘制直方图时，如果将`hist`函数的`density`参数修改为`True`，同时将`cumulative`参数也修改为`True`，
# # 那么一方面纵轴会显示为概率密度，而图表会绘制概率的累计分布
# plt.hist(heights,bins=np.arange(145,196,5),color='deeppink',density=True,cumulative=True)
# # 定制横轴标签
# plt.xlabel('身高')
# # 定制纵轴标签
# plt.ylabel('概率密度')
# plt.show()

# #### 箱线图

# 箱线图又叫箱型图或盒须图，是一种用于展示一组数据分散情况的统计图表
# 数组中有47个[0, 100)范围的随机数
data = np.random.randint(0,100,47)
# 向数组中添加三个可能是离群点的数据
data = np.append(data,160)
data = np.append(data,200)
data = np.append(data,-50)
plt.figure(figsize=(8,4),dpi=120)
# whis参数的默认值是1.5，将其设置为3可以检测极端离群值，showmeans=True表示在图中标记均值的位置
plt.boxplot(data,whis=1.5,showmeans=True,notch=True) # notch就是缺口的意思
# 定制纵轴的取值范围
plt.ylim([-100, 250])
# 定制横轴的刻度
plt.xticks([1], labels=['data'])
plt.show()

