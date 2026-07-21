import pandas as pd
import numpy as np

# 1.范围索引
# 范围索引是由具有单调性的整数构成的索引，我们可以通过`RangeIndex`构造器来创建范围索引，也可以通过`RangeIndex`类的类方法`from_range`来创建范围索引
sales_data = np.random.randint(400,1000,12)
index = pd.RangeIndex(1,13,name='月份')
ser = pd.Series(index=index,data=sales_data)
# print(ser)

# 2.分类索引
sales_data = [6, 6, 7, 6, 8, 6]
index = pd.CategoricalIndex(
    data=['苹果', '香蕉', '苹果', '苹果', '桃子', '香蕉'],
    categories=['苹果', '香蕉', '桃子'],
    ordered=True
)

ser = pd.Series(data=sales_data,index=index)
# print(ser)
# 修改索引的顺序
ser.index = index.reorder_categories(['香蕉', '桃子', '苹果'])
# print(ser.groupby(level=0).sum())

### 多级索引

# Pandas 中的`MultiIndex`类型用来表示层次或多级索引。可以使用`MultiIndex`类的类方法`from_arrays`、`from_product`、`from_tuples`等来创建多级索引，
# 用元组列表来创建索引
tuples = [(1, 'red'), (1, 'blue'), (2, 'red'), (2, 'blue')]
index = pd.MultiIndex.from_tuples(tuples,names=['no','color'])
# print(index)
# 用列表来创建索引
arrays = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]
index = pd.MultiIndex.from_arrays(arrays,names=['no','color'])
# print(index)

#  pd.MultiIndex.from_product(...)
stu_id = np.arange(1001,1006)
semisters = ['期中', '期末']
index = pd.MultiIndex.from_product((stu_id,semisters),names=['学号','学期'])
courses = ['语文','数学','英语']
scores = np.random.randint(60,101,(10,3))
df = pd.DataFrame(index=index,data=scores,columns=courses)
# print(df)
# 根据第一级索引分组数据，按照期中成绩占`25%`，期末成绩占`75%` 的方式计算每个学生每门课的成绩
# print(df.groupby(level=0).agg(lambda x:x.values[0]*0.25 + x.values[1]*0.75))

### 间隔索引

# 间隔索引顾名思义是使用固定的间隔范围充当索引，我们通常会使用`interval_range`函数来创建间隔索引，代码如下所示。
index = pd.interval_range(start=0,end=5)
# print(index) # IntervalIndex([(0, 1], (1, 2], (2, 3], (3, 4], (4, 5]], dtype='interval[int64, right]')
# print(index.contains(1.5)) # [False  True False False False]
# print(index.overlaps(pd.Interval(1.5,3.5))) # [False  True  True  True False]

#如果希望间隔范围是左闭右开的状态，可以在创建间隔索引时通过`closed='left'`来做到；如果希望两边都是关闭状态，可以将`close`参数的值赋值为`both`
index = pd.interval_range(start=0, end=5, closed='left')
# print(index) # IntervalIndex([[0, 1), [1, 2), [2, 3), [3, 4), [4, 5)], dtype='interval[int64, left]')
index = pd.interval_range(start=pd.Timestamp('2022-01-01'), end=pd.Timestamp('2022-01-04'), closed='both')
# print(index)
'''
IntervalIndex([[2022-01-01 00:00:00, 2022-01-02 00:00:00],
               [2022-01-02 00:00:00, 2022-01-03 00:00:00],
               [2022-01-03 00:00:00, 2022-01-04 00:00:00]],
              dtype='interval[datetime64[us], both]')

'''

### 日期时间索引

# `DatetimeIndex`应该是众多索引中最复杂最重要的一种索引，我们通常会使用`date_range()`函数来创建日期时间索引，
# 该函数有几个非常重要的参数`start`、`end`、`periods`、`freq`、`tz`，分别代表起始日期时间、结束日期时间、生成周期、采样频率和时区。
# 我们先来看看如何创建`DatetimeIndex`对象，再来讨论它的相关运算和操作
dt_index = pd.date_range('2021-1-1', '2021-6-30', periods=10)
# print(dt_index)

'''
DatetimeIndex(['2021-01-01', '2021-01-21', '2021-02-10', '2021-03-02',
               '2021-03-22', '2021-04-11', '2021-05-01', '2021-05-21',
               '2021-06-10', '2021-06-30'],
              dtype='datetime64[us]', freq=None)
'''

dt_index = pd.date_range('2021-1-1', '2021-6-30', freq='W')
# print(dt_index)

'''
DatetimeIndex(['2021-01-03', '2021-01-10', '2021-01-17', '2021-01-24',
               '2021-01-31', '2021-02-07', '2021-02-14', '2021-02-21',
               '2021-02-28', '2021-03-07', '2021-03-14', '2021-03-21',
               '2021-03-28', '2021-04-04', '2021-04-11', '2021-04-18',
               '2021-04-25', '2021-05-02', '2021-05-09', '2021-05-16',
               '2021-05-23', '2021-05-30', '2021-06-06', '2021-06-13',
               '2021-06-20', '2021-06-27'],
              dtype='datetime64[us]', freq='W-SUN')
'''
# print(dt_index - pd.DateOffset(days=2))

'''
DatetimeIndex(['2021-01-01', '2021-01-08', '2021-01-15', '2021-01-22',
               '2021-01-29', '2021-02-05', '2021-02-12', '2021-02-19',
               '2021-02-26', '2021-03-05', '2021-03-12', '2021-03-19',
               '2021-03-26', '2021-04-02', '2021-04-09', '2021-04-16',
               '2021-04-23', '2021-04-30', '2021-05-07', '2021-05-14',
               '2021-05-21', '2021-05-28', '2021-06-04', '2021-06-11',
               '2021-06-18', '2021-06-25'],
              dtype='datetime64[us]', freq=None)
'''
# print(dt_index + pd.DateOffset(hours=2,minutes=20))

'''
DatetimeIndex(['2021-01-03 02:20:00', '2021-01-10 02:20:00',
               '2021-01-17 02:20:00', '2021-01-24 02:20:00',
               '2021-01-31 02:20:00', '2021-02-07 02:20:00',
               '2021-02-14 02:20:00', '2021-02-21 02:20:00',
               '2021-02-28 02:20:00', '2021-03-07 02:20:00',
               '2021-03-14 02:20:00', '2021-03-21 02:20:00',
               '2021-03-28 02:20:00', '2021-04-04 02:20:00',
               '2021-04-11 02:20:00', '2021-04-18 02:20:00',
               '2021-04-25 02:20:00', '2021-05-02 02:20:00',
               '2021-05-09 02:20:00', '2021-05-16 02:20:00',
               '2021-05-23 02:20:00', '2021-05-30 02:20:00',
               '2021-06-06 02:20:00', '2021-06-13 02:20:00',
               '2021-06-20 02:20:00', '2021-06-27 02:20:00'],
              dtype='datetime64[us]', freq=None)
'''

stock_df = pd.read_excel("./2022_stocks.xlsx",sheet_name='BIDU', index_col='Date')
stock_df.sort_index(inplace=True)
# print(stock_df.asfreq('5D'))
# print(stock_df.asfreq('5D',method='ffill'))
# print(stock_df.resample('1ME').mean())
# print(stock_df.resample('1ME').agg(['mean','std']))

# 如果要实现日期时间的时区转换，我们可以先用`tz_localize()`方法将日期时间本地化
stock_df = stock_df.tz_localize("Asia/Shanghai")
# print(stock_df)

# 在对时间本地化以后，我们再使用`tz_convert()`方法就可以实现转换时区
stock_df = stock_df.tz_convert("America/New_York")
print(stock_df)