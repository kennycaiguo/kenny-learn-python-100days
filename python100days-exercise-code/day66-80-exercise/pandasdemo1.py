import numpy as np
import pandas as pd

s1 = pd.Series(data=[1000,2000,3000,4000],index=['第一季度','第二季度','第三季度','第四季度'])
# print(s1)
s2 = pd.Series({'第一季度':500,'第二季度':600,'第三季度':700,'第四季度':800})
# print(s2)

# print(s1+s2) # 2个Series相加就是把他们对应位置的元素相加
# print(s1+100) # Series + 一个数就是把他的每一个元素都+这个数
# print(s1[2]) # key error
# print(s1['第一季度']) # 1000
# print(s1[1:3]) # 切片索引 ok
# print(s2['第二季度':'第四季度']) # 这个和使用整数的切片不太一样，它连最后一个都包含了
# print(s2[['第二季度','第四季度']]) # 注意，这个不是切片，是花式索引

# print(s1[s1<4000])
# # if you want to use the integer index,use iloc or loc
# print(s1.iloc[2])
# print(s1.loc['第二季度'])
# # slice index
# print(s1[1:3])
# # list index
# print(s1[['第一季度','第三季度']])
# # boolean index
# print(s1[s1<3000])

# Series Properties
# 1.dtype
# print(s1.dtype) # int64

# 2.hasnans property ,not method
# print(s1.hasnans) # False

# 3.at/iat,in this case
# print(s1.iat[1]) # 2000
# 4.loc/iloc
# print(s1.iloc[2]) # 3000

# 5.index,return index of a Series object
# print(s1.index) # Index(['第一季度', '第二季度', '第三季度', '第四季度'], dtype='str')
     
# 6.`is_monotonic_increasing` | 判断`Series`对象中的数据是否单调递增 |
# print(s1.is_monotonic_increasing) #True
# 7.`is_monotonic_decreasing` |    
# print(s1.is_monotonic_decreasing)   # False    
  
# 8.is_unique      
# print(s1.is_unique) # True
# 9.size
# print(s1.size) # 4

# 10.values
# print(s1.values) # [1000 2000 3000 4000]

# Series Methods
# print(s1.count())
# print(s1.sum())
# print(s1.mean())
# print(s1.median())
# print(s1.max())
# print(s1.min())
# Standard deviation 标准差
# print(s1.std())
#variance 方差
# print(s1.var())

# print(s1.describe()) # count(),std(),min(),max(),25%,50%,75%
# print(s1.value_counts()) # get the count of each value inside a Series
# print(s1.nunique())
# print(s1.mode())
ser3 = pd.Series(data=['apple', 'banana', 'apple', 'pitaya', 'apple', 'pitaya', 'durian'])
# print(ser3.mode()) # 0    apple
ser4 = pd.Series(data=[10, 20, np.nan, 30, np.nan])
# print(ser4.isna())
# print(ser4.notna())
# print(ser4[ser4.notna()])
# print(ser4.dropna()) # create a new Series,doesn't change the original Series
# print(ser4)
# print(ser4.fillna(value=0)) # # create a new Series,doesn't change the original Series
# print(ser4)
# ser4.fillna(0,inplace=True)
# print(ser4)

ser5 = pd.Series(range(5))
# print(ser5.where(ser5>1,10)) # # create a new Series,doesn't change the original Series
# print(ser5)
# print(ser5.mask(ser5 > 1,10))
# print(ser5)

# print(ser3.duplicated())
ser3_new = ser3.drop_duplicates() # create a new Series,doesn't change the original Series
# print(ser3_new)

## apply() and map()
mapped = ser3_new .map({"apple":10,"banana":15,"pitaya":20,"durian":25})
# print(mapped)
# print(ser3_new.map('I am a {}'.format))
import math
# print(s1.apply(math.sqrt))
# print(s1.apply(lambda x,val:x-val,args=(500,)))

ser8 = pd.Series(
    data=[35, 96, 12, 57, 25, 89], 
    index=['grape', 'banana', 'pitaya', 'apple', 'peach', 'orange']
)

# print(ser8.sort_values(ascending=False))
# print(ser8.nlargest(2)) # n largest items
# print(ser8.nsmallest(3))  # n smallest items

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

ser9 = pd.Series({'Q1': 400, 'Q2': 520, 'Q3': 180, 'Q4': 380})
# 通过plot方法的kind指定图表类型为柱状图
# ser9.plot(kind='bar')
# # set the lim
# plt.ylim(0,600)
# # 定制横轴刻度（旋转到0度）
# plt.xticks(rotation=0)
# # 为柱子增加数据标签
# for i in range(ser9.size):
#     plt.text(i, ser9.iloc[i] + 5, ser9.iloc[i], ha='center')
# plt.show()

# 通过plot方法的kind指定图表类型为柱状图
# ser9.plot(kind='barh')
# # set the lim
# plt.xlim(0,600)
# # 定制横轴刻度（旋转到0度）
# plt.yticks(rotation=0)
# # 为柱子增加数据标签
# for i in range(ser9.size):
#     plt.text(i, ser9.iloc[i] + 5, ser9.iloc[i], ha='center')
# plt.show()

ser9.plot(kind='pie', autopct='%.1f%%', pctdistance=0.65)
plt.show()