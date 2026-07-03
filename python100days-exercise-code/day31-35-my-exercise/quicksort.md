# Python 快速排序

[![Document 对象参考手册](https://www.runoob.com/images/up.gif) Python3 实例](https://www.runoob.com/python3/python3-examples.html)

快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为较小和较大的2个子序列，然后递归地排序两个子序列。

步骤为：

- 挑选基准值：从数列中挑出一个元素，称为"基准"（pivot）;
- 分割：重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（与基准值相等的数可以到任何一边）。在这个分割结束之后，对基准值的排序就已经完成;
- 递归排序子序列：递归地将小于基准值元素的子序列和大于基准值元素的子序列排序。

递归到最底部的判断条件是数列的大小是零或一，此时该数列显然已经有序。

选取基准值有数种具体方法，此选取方法对排序的时间性能有决定性影响。

![img](https://www.runoob.com/wp-content/uploads/2019/03/quickSort.gif)

## 

1：首先取序列第一个元素为基准元素pivot=R[low]。i=low,j=high。 2：从后向前扫描，找小于等于pivot的数，如果找到，R[i]与R[j]交换，i++。 3：从前往后扫描，找大于pivot的数，如果找到，R[i]与R[j]交换，j--。 4:重复2~3，直到i=j,返回该位置mid=i,该位置正好为pivot元素。 完成一趟排序后，以mid为界，将序列分为两部分，左序列都比pivot小，有序列都比pivot大，然后再分别对这两个子序列进行快速排序。

以序列（30，24，5，58，18，36，12，42，39）为例，进行演示

> 1、初始化，i=low,j=high,pivot=R[low]=30

![img](https://pic2.zhimg.com/v2-1b70972793de6f7003581303d1c0a01b_1440w.jpg)

> 2、从后往前找小于等于pivot的数，找到R[j]=12

![img](https://pic1.zhimg.com/v2-a46c93bd2c6ab8f11cf8cc0618142cea_1440w.jpg)

R[i]与R[j]交换，i++

![img](https://pic2.zhimg.com/v2-23e3f6ce378b1a6bafd66acd95f9cbd7_1440w.jpg)

> 3、从前往后找大于pivot的数，找到R[i]=58

![img](https://picx.zhimg.com/v2-11322684cb8a141c99f1e5fc4600efab_1440w.jpg)

R[i]与R[j]交换，j--

![img](https://pic1.zhimg.com/v2-b3318ede73bcd4ea9469d531c7a08aea_1440w.jpg)

> 4、从后往前找小于等于pivot的数，找到R[j]=18

![img](https://picx.zhimg.com/v2-dc85df07b12e8f60bbaacf4e6051ab7f_1440w.jpg)

R[i]与R[j]交换，i++

![img](https://pic1.zhimg.com/v2-8928f6cb5290feed2a0c36cfa42a8c12_1440w.jpg)

> 5、从前往后找大于pivot的数，这时i=j,第一轮排序结束，返回i的位置，mid=i

![img](https://picx.zhimg.com/v2-bae9a5d0ae1dfce47a88d69de519147b_1440w.jpg)

此时已mid为界，将原序列一分为二，左子序列为（12，24，5，18）元素都比pivot小，右子序列为（36，58，42，39）元素都比pivot大。然后在分别对两个子序列进行快速排序，最后即可得到排序后的结果。

> **复杂度分析**

- **最好的[时间复杂度](https://zhida.zhihu.com/search?content_id=102180078&content_type=Article&match_order=1&q=时间复杂度&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODEzNTUwOTIsInEiOiLml7bpl7TlpI3mnYLluqYiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoxMDIxODAwNzgsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.4yzT1lr-MJltpanlDNTJ5PDiDn5MYYJnxAGvY6bPJ30&zhida_source=entity)为：O(nlogn)**

分解：划分函数需要扫描每个元素，每次扫描元素不超过n，时间复杂度为O(n) 解决子问题：在理想的情况下，每次划分将问题分解为两个规模为n/2的子问题，递归求解两个规模的子问题。所需时间为2T(n/2) 合并：因为是原地排序，合并不需要时间复杂度 因此总运行时间为

```text
T(n)={ O(1) , n=1
    2T(n/2)+O(n) , n>1 }
```

最终求解为最好的时间复杂度为O(nlogn)

- **最坏的时间复杂度为: O(n²)**

> 分解：划分函数需要扫描每个元素，每次扫描元素不超过n，时间复杂度为O(n) 解决子问题：在最坏的情况下，每次划分将问题分解后，基准元素的一侧没有元素，其中一侧为规模为n-1的子问题，递归求解该子问题，所需时间为T(n-1)。 合并：因为是原地排序，合并不需要时间复杂度 因此总运行时间为

```text
T(n)={ O(1) , n=1
        T(n-1)+O(n) , n>1 }
```

最终求解为最好的时间复杂度为O(n²)

- **平均时间复杂度为：O(nlogn)**
- **平均[空间复杂度](https://zhida.zhihu.com/search?content_id=102180078&content_type=Article&match_order=1&q=空间复杂度&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODEzNTUwOTIsInEiOiLnqbrpl7TlpI3mnYLluqYiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoxMDIxODAwNzgsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.6oIvaudA2b8L2LCBDxAo8LdpTiEpU9ff7J0QmfTKPWA&zhida_source=entity)为：O(logn)**

> **python实现**

```python3
def quick_sort(lists,i,j):
    if i >= j:
        return list
    pivot = lists[i]
    low = i
    high = j
    while i < j:
        while i < j and lists[j] >= pivot:
            j -= 1
        lists[i]=lists[j]
        while i < j and lists[i] <=pivot:
            i += 1
        lists[j]=lists[i]
    lists[j] = pivot
    quick_sort(lists,low,i-1)
    quick_sort(lists,i+1,high)
    return lists

if __name__=="__main__":
    lists=[30,24,5,58,18,36,12,42,39]
    print("排序前的序列为：")
    for i in lists:
        print(i,end =" ")
    print("\n排序后的序列为：")
    for i in quick_sort(lists,0,len(lists)-1):
        print(i,end=" ")

>>>
排序前的序列为：
30 24 5 58 18 36 12 42 39
排序后的序列为：
5 12 18 24 30 36 39 42 58
```

## 实例2

```
def quicksort(array):
    size = len(array)
    if not array or size < 2:  # NOTE: 递归出口，空数组或者只有一个元素的数组都是有序的
        return array
    pivot_idx = 0
    pivot = array[pivot_idx]
    less_part = [array[i] for i in range(size) if array[i] <= pivot and pivot_idx != i]
    great_part = [array[i] for i in range(size) if array[i] > pivot and pivot_idx != i]
    return quicksort(less_part) + [pivot] + quicksort(great_part)


print("排序前的序列为:")
for i in lists:
    print(i,end =" ")
print("\n排序后的序列为:")
for i in quicksort(lists):
    print(i,end=" ")
```

### 结果

排序前的序列为:
30 24 5 58 18 36 12 42 39 
排序后的序列为:
5 12 18 24 30 36 39 42 58 