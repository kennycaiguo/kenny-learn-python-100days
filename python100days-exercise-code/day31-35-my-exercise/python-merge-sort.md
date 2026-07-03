归并排序（英语：Merge sort，或mergesort），是创建在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。

分治法:

- 分割：递归地把当前序列平均分割成两半。
- 集成：在保持元素顺序的同时将上一步得到的子序列集成到一起（归并）。

![img](https://www.runoob.com/wp-content/uploads/2019/03/mergeSort.gif)

### 图解2

![img](https://img2018.cnblogs.com/blog/1400528/201905/1400528-20190501210011723-1953669437.png)

## 实例

```
#归并排序（MERGE-SORT）
def merge_sort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr) //2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left),merge_sort(right))

def merge(arr1,arr2):
    result = []
    while len(arr1)>0 and len(arr2)>0:
        if arr1[0] < arr2[0]:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))    
    result += arr1
    result += arr2
    return result

arr = [10,2,3,5,7,6,9,8]
print(merge_sort(arr))
```

### result

```
[2, 3, 5, 6, 7, 8, 9, 10]
```

