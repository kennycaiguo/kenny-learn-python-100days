"""set"""
#1 create 空的集合,只能够使用set(),不能够使用x = {}，英文{}代表空的字典
s = set()
d = {}
print(type(s)) # <class 'set'>
print(type(d)) # <class 'dict'>

# set里面的数据类型：整数（int）、浮点小数（float）、布尔值（bool）、字符串（str）、元组（tuple）
# set里面不能嵌套list，也不嵌套set,也不能嵌套字典
# s = {[1,2,3],[4,5,6]} #TypeError: unhashable type: 'list'
# s = {{1,2},{3,4}} # TypeError: unhashable type: 'set'
# s = {{"name":"jack"},{"age":18}} # TypeError: unhashable type: 'dict'
# 遍历
# set1 = {'Python', 'C++', 'Java', 'Kotlin', 'Swift'}
# for elem in set1:
#     print(elem)

"""
集合的运算
Python 为集合类型提供了非常丰富的运算，主要包括：成员运算、交集运算、并集运算、差集运算、比较运算（相等性、子集、超集）等。

成员运算
可以通过成员运算in和not in 检查元素是否在集合中，代码如下所示。

set1 = {11, 12, 13, 14, 15}
print(10 in set1)      # False 
print(15 in set1)      # True
set2 = {'Python', 'Java', 'C++', 'Swift'}
print('Ruby' in set2)  # False
print('Java' in set2)  # True
二元运算
集合的二元运算主要指集合的交集、并集、差集、对称差等运算，这些运算可以通过运算符来实现，也可以通过集合类型的方法来实现，代码如下所示。



"""
# set1 = {1, 2, 3, 4, 5, 6, 7}
# set2 = {2, 4, 6, 8, 10}

# # 交集
# print(set1 & set2)                      # {2, 4, 6}
# print(set1.intersection(set2))          # {2, 4, 6}

# # 并集
# print(set1 | set2)                      # {1, 2, 3, 4, 5, 6, 7, 8, 10}
# print(set1.union(set2))                 # {1, 2, 3, 4, 5, 6, 7, 8, 10}

# # 差集
# print(set1 - set2)                      # {1, 3, 5, 7}
# print(set1.difference(set2))            # {1, 3, 5, 7}

# # 对称差
# print(set1 ^ set2)                      # {1, 3, 5, 7, 8, 10}
# print(set1.symmetric_difference(set2))  # {1, 3, 5, 7, 8, 10}

"""
通过上面的代码可以看出，对两个集合求交集，&运算符和intersection方法的作用是完全相同的，
使用运算符的方式显然更直观且代码也更简短。需要说明的是，集合的二元运算还可以跟赋值运算一起构成复合赋值运算，
例如：set1 |= set2相当于set1 = set1 | set2，跟|=作用相同的方法是update；set1 &= set2相当于set1 = set1 & set2，
跟&=作用相同的方法是intersection_update，代码如下所示。
"""
# set1 = {1, 3, 5, 7}
# set2 = {2, 4, 6}
# set1 |= set2
# # set1.update(set2)
# print(set1)  # {1, 2, 3, 4, 5, 6, 7}
# set3 = {3, 6, 9}
# set1 &= set3
# # set1.intersection_update(set3)
# print(set1)  # {3, 6}
# set2 -= set1
# # set2.difference_update(set1)
# print(set2)  # {2, 4}
"""
比较运算
两个集合可以用==和!=进行相等性判断，如果两个集合中的元素完全相同，那么==比较的结果就是True，否则就是False。如果集合A的任意一个元素都是集合B的元素，那么集合A称为集合B的子集，即对于 
∀
a
∈
A
 ，均有 
a
∈
B
 ，则 
A
⊆
B
 ，A是B的子集，反过来也可以称B是A的超集。如果A是B的子集且A不等于B，那么A就是B的真子集。
 Python 为集合类型提供了判断子集和超集的运算符，其实就是我们非常熟悉的<、<=、>、>=这些运算符。
 当然，我们也可以通过集合类型的方法issubset和issuperset来判断集合之间的关系，代码如下所示。
"""
# set1 = {1, 3, 5}
# set2 = {1, 2, 3, 4, 5}
# set3 = {5, 4, 3, 2, 1}

# print(set1 < set2)   # True
# print(set1 <= set2)  # True
# print(set2 < set3)   # False
# print(set2 <= set3)  # True
# print(set2 > set1)   # True
# print(set2 == set3)  # True

# print(set1.issubset(set2))    # True
# print(set2.issuperset(set1))  # True

"""
说明：上面的代码中，set1 < set2判断set1是不是set2的真子集，set1 <= set2判断set1是不是set2的子集，set2 > set1判断set2是不是set1的超集。
当然，我们也可以通过set1.issubset(set2)判断set1是不是set2的子集；通过set2.issuperset(set1)判断set2是不是set1的超集。
"""
# 集合的方法
# 刚才我们说过，Python 中的集合是可变类型，我们可以通过集合的方法向集合添加元素或从集合中删除元素。
# set1 = {1, 10, 100}

# # 添加元素
# set1.add(1000)
# set1.add(10000)
# print(set1)  # {1, 100, 1000, 10, 10000}

# # 删除元素
# set1.discard(10)
# if 100 in set1:
#     set1.remove(100)
# print(set1)  # {1, 1000, 10000}

# # 清空元素
# set1.clear()
# print(set1)  # set()
"""
说明：删除元素的remove方法在元素不存在时会引发KeyError错误，所以上面的代码中我们先通过成员运算判断元素是否在集合中。
集合类型还有一个pop方法可以从集合中随机删除一个元素，该方法在删除元素的同时会返回（获得）被删除的元素，而remove和discard方法仅仅是删除元素，
不会返回（获得）被删除的元素。
"""

# 不可变集合
# Python 中还有一种不可变类型的集合，名字叫frozenset。set跟frozenset的区别就如同list跟tuple的区别，frozenset由于是不可变类型，
# 能够计算出哈希码，因此它可以作为set中的元素。除了不能添加和删除元素，frozenset在其他方面跟set是一样的，下面的代码简单的展示了frozenset的用法。

fset1 = frozenset({1, 3, 5, 7})
fset2 = frozenset(range(1, 6))
print(fset1)          # frozenset({1, 3, 5, 7})
print(fset2)          # frozenset({1, 2, 3, 4, 5})
print(fset1 & fset2)  # frozenset({1, 3, 5})
print(fset1 | fset2)  # frozenset({1, 2, 3, 4, 5, 7})
print(fset1 - fset2)  # frozenset({7})
print(fset1 < fset2)  # False
# 总结
# Python 中的集合类型是一种无序容器，不允许有重复运算，由于底层使用了哈希存储，集合中的元素必须是hashable类型。
# 集合与列表最大的区别在于集合中的元素没有顺序、所以不能够通过索引运算访问元素、但是集合可以执行交集、并集、差集等二元运算，
# 也可以通过关系运算符检查两个集合是否存在超集、子集等关系。