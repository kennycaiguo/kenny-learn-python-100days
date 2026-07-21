import pandas as pd
import numpy as np

scores = np.random.randint(50, 101, (5, 3))
names = ('关羽', '张飞', '赵云', '马超', '黄忠')
courses = ('语文', '数学', '英语')
df = pd.DataFrame(data=scores,columns=courses,index=names)

# print(df)
# 计算科目评价分和每个学生的平均分
# print(df.mean())  # 计算每一科的平均成绩，这个是用行来做评价
# print(df.mean(axis=1)) #列评价，也就是每个学生的平均分
# 计算方差
# print(df.var())
# print(df.var(axis=1))

# 获取每门课程的描述性统计信息。
# print(df.describe())
# 排序
# print(df.sort_values(by='数学',ascending=False))

# nlargest,最大的前几个
# print(df.nlargest(2,'英语'))

#nsmallest,最小的前几个
# print(df.nsmallest(2,'语文'))

df = pd.read_excel('./sales.xlsx')
# print(df.head())
# print(df.columns.tolist())
# 注意：用excel作为pandas的数据需要清除多余的空格，否则会报错，查看是否有空格就可以使用print(df.columns.tolist())来检查
df['销售额'] =  df['售价'] * df['销售数量']
# print(df.head())
# print(df.groupby('销售区域').销售额.sum())
# print(df.groupby(df['销售日期'].dt.month).销售额.sum())
# print(df.groupby(['销售区域',df['销售日期'].dt.month]).销售额.sum())
# 如果希望统计出每个区域的销售总额以及每个区域单笔金额的最高和最低，
# 我们可以在`DataFrame`或`Series`对象上使用`agg`方法并指定多个聚合函数，代码和结果如下所示。
# print(df.groupby('销售区域').销售额.agg(['sum','max','min','mean']))
# 如果希望自定义聚合后的列的名字，可以使用如下所示的方法
# print(df.groupby('销售区域').销售额.agg(销售总额='sum', 单笔最高='max', 单笔最低='min'))
# 如果需要对多个列使用不同的聚合函数，例如“统计每个销售区域销售额的总和以及销售数量的最低值和最高值”，我们可以按照下面的方式来操作。
# print(df.groupby('销售区域')[['销售额','销售数量']].agg({'销售额':'sum','销售数量':['max',"min"]}))

# 透视表和交叉表
# 透视表
# print(pd.pivot_table(df,index='销售区域',values='销售额',aggfunc='sum')) # 效果和groupby差不多，但是这里的结果类型是DataFrame而groupby得到的是Series

# 给dataframe添加一个月份列
df['月份'] = df['销售日期'].dt.month
# 然后按月份来做
# print(pd.pivot_table(df,index='销售区域',columns='月份',values='销售额',aggfunc='sum',fill_value=0))
# print(pd.pivot_table(df,index='销售区域',columns='月份',values='销售额',aggfunc='sum',fill_value=0,margins=True,margins_name='总计'))
# 使用`crosstab`函数生成交叉表。
sales_area, sales_month, sales_amount = df['销售区域'], df['月份'], df['销售额']
# print(pd.crosstab(index=sales_area,columns=sales_month,values=sales_amount,aggfunc='sum').fillna(0).astype('i8'))

# 数据可视化
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] =  ['SimHei']  # 设置matplotlib显示中文

table = pd.pivot_table(df,index='销售区域',values='销售额',aggfunc='sum')
# 柱状图
# table.plot(figsize=(8,4),kind='bar')
# plt.xticks(rotation=0)
# plt.show()
#饼图
# table.sort_values(by='销售额',ascending=False).plot(
#     figsize=(6,6),
#     kind='pie',
#     y='销售额',
#     autopct='%.2f%%', # 保留多少位小数
#     pctdistance = 0.78, # 设置百分比距离圆心的距离
#     wedgeprops=dict(linewidth=1,width=1), # width参数调整饼的大小取值0-1
#     legend=False
# )

# plt.show()

# 计算同比环比
p_table = df.pivot_table(index='月份',values='销售额',aggfunc='sum')
p_table.rename(columns={'销售额':"本月销售额"},inplace=True)
# print(p_table)
p_table['上月销售额'] = p_table.本月销售额.shift(1)
# print(p_table)
# 环比
p_table['环比'] = (p_table.本月销售额-p_table.上月销售额)/p_table.上月销售额
p_table.style.format(
    formatter={'上月销售额':'{:.0f}','环比':'{:.2%}'},
    na_rep='------------------'
)

# print(p_table)
# 计算环比还有另外一种方法，我们先把上面的环比删除
p_table.drop(columns=['上月销售额', '环比'], inplace=True)
p_table['环比'] = p_table.pct_change()
# print(p_table)

# rolling
stock_df = pd.read_excel("./2022_stocks.xlsx",sheet_name='BIDU', index_col='Date')
stock_df.sort_index(inplace=True)
# print(stock_df)
# print(stock_df.rolling(5).mean())
# 我们可以对上面的百度股票收盘价（`Close`列）计算5日均线和10日均线，并使用`merge`函数将其组装到一个`DataFrame`对象中并绘制出双均线图
close_ma5 = stock_df.Close.rolling(5).mean()
close_ma10 = stock_df.Close.rolling(10).mean()

stock_df = pd.merge(close_ma5,close_ma10,left_index=True,right_index=True)
stock_df.rename(columns={'Close_x':'MA5','Close_y':'MA10'},inplace=True)
# stock_df.plot(kind='line',figsize=(10,6))
# plt.show()

# boston housing
boston_df = pd.read_csv("./boston_house_price.csv")
# print(boston_df.head())
# print(boston_df[['NOX', 'RM', 'PTRATIO', 'LSTAT', 'PRICE']].corr())
boston_df['CRIM'] = boston_df.CRIM.apply(lambda x: x//5 if x<25 else 5).map(int)
boston_df['ZN'] = pd.qcut(boston_df.ZN,q=[0, 0.75, 0.8, 0.85, 0.9, 0.95, 1],labels=np.arange(6))
boston_df['AGE'] = (boston_df.AGE // 20).map(int)
boston_df['DIS'] = (boston_df.DIS // 2.05).map(int)
boston_df['B'] = (boston_df.B //66).map(int)
boston_df['PRICE'] = pd.qcut(boston_df.PRICE,q=[0, 0.15, 0.3, 0.5, 0.7, 0.85, 1],labels=np.arange(6))
print(boston_df[['CRIM','ZN','AGE','DIS','B','PRICE']].corr(method='spearman'))

