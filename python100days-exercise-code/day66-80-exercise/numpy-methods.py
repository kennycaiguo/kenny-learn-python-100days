import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

nums = np.random.randint(1,100,12)
# print(nums)
## 1.
# # get the sum
# print(nums.sum())
# print(np.sum(nums))
# # get avarage
# print(nums.mean())
# print(np.mean(nums))
# # median,only has one way np.median(arr)
# print(np.median(nums))
# # 分位数,only has one way np.quantile(arr,q)
# print(np.quantile(nums,0.3))

## 2.max,min,...
#极值、
# 全距amin() toplevel function,only can use by np.amin(arr)
# 四分位距离ptp
# print(nums.max())
# print(nums.min())
# print(np.amin(nums))
# print(np.ptp(nums))
# q1,q2 = np.quantile(nums,[0.25,0.75])
# print(q1,q2)
# print(q2-q1)

## 3.var,std,std()/mean()
# print(nums.var())
# print(np.var(nums))
# print(nums.std())
# print(np.std(nums))
# ratio = nums.std()/nums.mean()
# print(ratio)

## 4.boxplot,a pyplot function
# plt.boxplot(nums,showmeans=True)
# plt.ylim(-20,120)
# plt.show()

nums2 = np.random.randint(1,100,(5,3))
# print(nums2)
# plt.boxplot(nums2,showmeans=True)
# plt.ylim(-20,120)
# plt.show()

# NumPy 的数组对象并没有提供计算几何平均值、调和平均值、去尾平均值等的方法，如果有这方面的需求，可以使用名为 scipy 的三方库，它的`stats`模块中提供了这些函数。
# 此外，该模块还提供了计算众数、变异系数、偏态、峰度的函数
from scipy import stats

# print(stats.gmean(nums2))  # 几何平均值
# print(stats.hmean(nums2))  # 调和平均值
# print(stats.tmean(nums2,[10,90])) # 去尾平均值
# print(stats.variation(nums2))        # 变异系数
# print(stats.skew(nums2))             # 偏态系数
# print(stats.kurtosis(nums2))         # 峰度系数

# `dump()`方法：保存数组到二进制文件中
nums2.dump('nums2')
# 可以通过 NumPy 中的`load()`函数从保存的文件中加载数据创建数组,注意需要传递allow_pickle=True否则抛异常
arr = np.load('nums2',allow_pickle=True)
# print(arr)
# `tofile()`方法：将数组对象写入文本文件中
# arr.tofile("arr.txt",sep=',')
# `swapaxes()`和`transpose()`方法：交换数组指定的轴和转置。
print("==================")
# arr2 = arr.swapaxes(0,1) # 把x轴和y轴互换，5行3列的数组就会变为3行5列的数组。注意这个方法不改变源数组
# print(arr2)
# arr3 = arr.transpose() # 把x轴和y轴互换，5行3列的数组就会变为3行5列的数组。注意这个方法不改变源数组
# print("-----------------------------------")
# print(arr3)

# p3 = np.poly1d([1, 3, 2])
# print(p3.roots)

# numpy matrix
m1 = np.matrix('1 2 3; 4 5 6 ; 7 8 9')
# print(m1)

arr = np.array([[10,20,30],[11,22,33],[31,32,33]])
m = np.asmatrix(arr)
# print(m,type(m)) # asmatrix: toplevel function

# print(m.A)
# print(m.A1) # flattern array [10 20 30 11 22 33 31 32 33]
# print(m.I) # Invertible matrix,error
# print(np.linalg.pinv(m)) # ???
# print(m.T)
# print(m.H)
# print(m.shape)
# print(m.size) # the total elements count: 9

p1 = np.poly1d([3,2,1])
print(p1)
p2 = np.poly1d([1,2,3])
print(p2)
print("=====================")
# print(p1.coefficients)
# print(p1.coeffs)
# print(p1.coef)

# print(p1+p2) # 4 x + 4 x + 4
print(p1*p2) # 3 x + 8 x + 14 x + 8 x + 3
