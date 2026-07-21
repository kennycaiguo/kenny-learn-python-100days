import seaborn as sbn
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'].insert(0, 'SimHei')
plt.rcParams['axes.unicode_minus'] = False

tips_df = sbn.load_dataset('tips')
# print(tips_df.info())

# 如果我们希望了解账单金额的分布，可以使用下面的代码来绘制分布图
# sbn.histplot(data=tips_df, x='total_bill', kde=True)
# plt.show() # 用seaborn绘制的图形也需要pyplot来显示

# 如果想了解变量之间的两两关系，我们可以绘制点对图
# sbn.pairplot(data=tips_df,hue='sex')
# plt.show()

# 修改调色板颜色
# sbn.set_palette('Dark2')
# sbn.pairplot(data=tips_df,hue='sex',palette='Dark2')
# sbn.set_palette('husl')
# sbn.pairplot(data=tips_df,hue='sex',palette='husl')
# sbn.set_palette('Set2')
# sbn.pairplot(data=tips_df,hue='sex',palette='Set2')
# sbn.set_palette('pastel')
# sbn.pairplot(data=tips_df,hue='sex',palette='pastel')
# plt.show()

# sbn.jointplot(data=tips_df,x='total_bill', y='tip', hue='sex')
# plt.show()

# sbn.lmplot(data=tips_df,x='total_bill', y='tip', hue='sex')
# plt.show()

# sbn.boxplot(data=tips_df,x='day', y='total_bill')
# plt.show()

sbn.violinplot(data=tips_df,x='day', y='total_bill')
plt.show()
