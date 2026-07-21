import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')
# 配置matplotlib显示中文
plt.rcParams['font.sans-serif'].insert(0, 'SimHei')
plt.rcParams['axes.unicode_minus'] = False

# 气泡图，也是使用scatter函数和散点图一样
income = np.array([5550, 7500, 10500, 15000, 20000, 25000, 30000, 40000])
outcome = np.array([800, 1800, 1250, 2000, 1800, 2100, 2500, 3500])
nums = np.array([5, 3, 10, 5, 12, 20, 8, 10])

# # 通过scatter函数的s参数和c参数分别控制面积和颜色
# plt.scatter(income, outcome, s=nums * 30, c=nums, cmap='Reds')
# # 显示颜色条
# plt.colorbar()
# # 显示图表
# plt.show()

### 面积图

# 面积图又叫堆叠折线图，是在折线图的基础上，对折线以下的区域进行颜色填充（展示面积），用于在连续间隔或时间跨度上展示数值，
# 一般用来显示趋势和对比数值，不同颜色的填充可以让多个面积块之间的对比和趋势更好的突显。
# 我们用面积图来展示从周一到周日花在睡觉、吃饭、工作和玩耍上的时间。
# plt.figure(figsize=(8, 4))
# days = np.arange(7)
# sleeping = [7, 8, 6, 6, 7, 8, 10]
# eating = [2, 3, 2, 1, 2, 3, 2]
# working = [7, 8, 7, 8, 6, 2, 3]
# playing = [8, 5, 9, 9, 9, 11, 9]
# # 绘制堆叠折线图
# plt.stackplot(days, sleeping, eating, working, playing)
# # 定制横轴刻度
# plt.xticks(days, labels=[f'星期{x}' for x in '一二三四五六日'])
# # 定制图例
# plt.legend(['睡觉', '吃饭', '工作', '玩耍'], fontsize=10)
# # 显示图表
# plt.show()

### 雷达图

# 雷达图通常用来比较多个定量数据，用于查看哪些变量具有相似的值
# labels = np.array(['速度', '力量', '经验', '防守', '发球', '技术'])
# # 马龙和水谷隼的数据
# malong_values = np.array([93, 95, 98, 92, 96, 97])
# shuigu_values = np.array([30, 40, 65, 80, 45, 60])
# angles = np.linspace(0, 2 * np.pi, labels.size, endpoint=False)
# # 多加一条数据让图形闭合
# malong_values = np.append(malong_values, malong_values[0])
# shuigu_values = np.append(shuigu_values, shuigu_values[0])
# angles = np.append(angles, angles[0])
# # 创建画布
# plt.figure(figsize=(4, 4), dpi=120)
# # 创建坐标系
# ax = plt.subplot(projection='polar')
# # 绘图和填充
# plt.plot(angles, malong_values, color='r', linewidth=2, label='马龙')
# plt.fill(angles, malong_values, color='r', alpha=0.3)
# plt.plot(angles, shuigu_values, color='g', linewidth=2, label='水谷隼')
# plt.fill(angles, shuigu_values, color='g', alpha=0.2)
# # 显示图例
# ax.legend()
# # 显示图表
# plt.show()

### 玫瑰图

# # 玫瑰图是映射在极坐标下的柱状图
# group1 = np.random.randint(20, 50, 4)
# group2 = np.random.randint(10, 60, 4)
# x = np.array([f'A组-Q{i}' for i in range(1, 5)] + [f'B组-Q{i}' for i in range(1, 5)])
# y = np.array(group1.tolist() + group2.tolist())
# # 玫瑰花瓣的角度和宽度
# theta = np.linspace(0, 2 * np.pi, x.size, endpoint=False)
# width = 2 * np.pi / x.size
# # 生成8种随机颜色
# colors = np.random.rand(8, 3)
# # 将柱状图投影到极坐标
# ax = plt.subplot(projection='polar')
# # 绘制柱状图
# plt.bar(theta, y, width=width, color=colors, bottom=0)
# # 设置网格
# ax.set_thetagrids(theta * 180 / np.pi, x, fontsize=10)
# # 显示图表
# plt.show()

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8, 4), dpi=120)
# 创建3D坐标系并添加到画布上
ax = Axes3D(fig,auto_add_to_figure=False) # 创建一个Axes3D类的一个对象
fig.add_axes(ax) # 把这个3D轴添加到画布
x = np.arange(-2, 2, 0.1)
y = np.arange(-2, 2, 0.1)
x, y = np.meshgrid(x, y)
z = (1 - y ** 5 + x ** 5) * np.exp(-x ** 2 - y ** 2)
# 绘制3D曲面
ax.plot_surface(x,y,z)
plt.show()