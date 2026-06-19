"""usage of Comprehension"""

def dict_comprehension():
    # dict Comprehension
    prices = {
        'AAPL': 191.88,
        'GOOG': 1186.96,
        'IBM': 149.24,
        'ORCL': 48.44,
        'ACN': 166.89,
        'FB': 208.09,
        'SYMC': 21.29
    }
    # 用股票价格大于100元的股票构造一个新的字典
    prices2 ={k:v for k,v in prices.items() if v >=100}
    print(prices2)

def list_comprehension():
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    courses = ['语文', '数学', '英语']
    # 录入五个学生三门课程的成绩
    scores = [[None] * len(courses) for _ in range(len(names))]
    for row, name in enumerate(names):
        for col, course in enumerate(courses):
            scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
            print(scores)


def heapq_demo():
    import heapq
    list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
    list2 = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]

    print(heapq.nlargest(5,list1))
    print(heapq.nsmallest(5,list1))
    print(heapq.nlargest(3,list2,key=lambda x:x["price"]))
    print(heapq.nsmallest(3,list2,key=lambda x:x["price"]))


import itertools

# print(list(itertools.permutations("ABCD"))) # input : ABCD output iter->[('A', 'B', 'C', 'D'),...., ('D', 'C', 'B', 'A')]
# print(list(itertools.combinations("ABCDE",3))) # pick up 3 out of "ABCDE" [('A', 'B', 'C'),...,('C', 'D', 'E')]
# print(list(itertools.product("ABCDE",'123'))) #[('A', '1'), ('A', '2'), ('A', '3'), ('B', '1'), ('B', '2'), ('B', '3'), ('C', '1'), ('C', '2'), ('C', '3'), ('D', '1'), ('D', '2'), ('D', '3'), ('E', '1'), ('E', '2'), ('E', '3')]
# print(list(itertools.cycle(('H','I')))) not good
# print(list(itertools.accumulate([1,2,3,4,5]))) # iter->list [1, 3, 6, 10, 15]
# reslt = list(itertools.chain([1,3,5],(2,4,6),{"a","b"}))
# print(reslt) #iterator - >list [1, 3, 5, 2, 4, 6, 'a', 'b']
# print(list(itertools.count(4))) #dangerous

from itertools import count

# for num in count(start=5, step=5):
#     if num > 20:
#         break # term to exit
#     print(num)

def select_sort(items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

num = [10,5,6,9,8,7]
# new_num = select_sort(num)
# print(new_num) # [5, 6, 7, 8, 9, 10]

def bubble_sort(items, comp=lambda x, y: x > y):
    """搅拌排序(冒泡排序升级版)"""
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items

# print(bubble_sort(num))

def bubble_sort0(items, comp=lambda x, y: x > y):
    """冒泡排序"""
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items

# print(bubble_sort0(num)) # [5, 6, 7, 8, 9, 10]
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

# arr = [10,2,3,5,7,6,9,8]
# print(merge_sort(arr))

def seq_search(items,key):
    for idx,val in enumerate(items):
        if val == key:
            return idx
        return -1 # not found
    
arr = [10,4,5,6,9]      
# print(seq_search(arr,5))   # position 2
# print(seq_search(arr,6))   # position 3
# print(seq_search(arr,10))  # position 0

def dive_fish():
    fish = 6
    while True:
        total = fish
        enough = True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                enough = False
                break
        if enough:
            print(fish) # 3121
            break
        fish += 5


# not the best idea,if you want the biggest number of things,yes,but if you want the biggest amount ,no
# can i get a better solution? 次程序的最优解是255，手工计算的是275
# clock + painting + book ，price：275 weight：20？
class Thing(object):
    """物品"""

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        """价格重量比"""
        return self.price / self.weight
       


def input_thing():
    """输入物品信息"""
    print("please enter things in detail")
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)


def main():
    """主函数"""
    print("please enter the total weight and total things")
    max_weight, num_of_things = map(int, input().split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))
    all_things.sort(key=lambda x: x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'小偷拿走了{thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'总价值: {total_price}美元')        

# main()

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

lists=[30,24,5,58,18,36,12,42,39]
# print("排序前的序列为:")
# for i in lists:
#     print(i,end =" ")
# print("\n排序后的序列为:")
# for i in quick_sort(lists,0,len(lists)-1):
#     print(i,end=" ")

def quicksort(array):
    size = len(array)
    if not array or size < 2:  # NOTE: 递归出口，空数组或者只有一个元素的数组都是有序的
        return array
    pivot_idx = 0
    pivot = array[pivot_idx]
    less_part = [array[i] for i in range(size) if array[i] <= pivot and pivot_idx != i]
    great_part = [array[i] for i in range(size) if array[i] > pivot and pivot_idx != i]
    return quicksort(less_part) + [pivot] + quicksort(great_part)


# print("排序前的序列为:")
# for i in lists:
#     print(i,end =" ")
# print("\n排序后的序列为:")
# for i in quicksort(lists):
#     print(i,end=" ")

import sys
import time

SIZE = 5
total = 0


def print_board(board):
    for row in board:
        for col in row:
            print(str(col).center(4), end='')
        print()


def patrol(board, row, col, step=1):
    if row >= 0 and row < SIZE and \
        col >= 0 and col < SIZE and \
        board[row][col] == 0:
        board[row][col] = step
        if step == SIZE * SIZE:
            global total
            total += 1
            print(f'第{total}种走法: ')
            print_board(board)
        patrol(board, row - 2, col - 1, step + 1)
        patrol(board, row - 1, col - 2, step + 1)
        patrol(board, row + 1, col - 2, step + 1)
        patrol(board, row + 2, col - 1, step + 1)
        patrol(board, row + 2, col + 1, step + 1)
        patrol(board, row + 1, col + 2, step + 1)
        patrol(board, row - 1, col + 2, step + 1)
        patrol(board, row - 2, col + 1, step + 1)
        board[row][col] = 0


def main():
    board = [[0] * SIZE for _ in range(SIZE)]
    patrol(board, SIZE - 1, SIZE - 1)

# main()

def maxinsub():
    items = list(map(int, input().split()))
    print(items)
    overall = partial = items[0]
    for i in range(1, len(items)):
        partial = max(items[i], partial + items[i])
        overall = max(partial, overall)
        print(overall,partial,items[i])
    print(overall)

# maxinsub()   

# 用__add__ 实现+ 如： obj3 = obj1 + obj2，注意他们必须是相同类型的对象
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x,new_y) 

v1 = Vector(10,20)
v2 = Vector(30,40)
v3 = v1 + v2
# print(v3.x,v3.y)

## 用 __eq__ 实现 == ，比如obj1 == obj2
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x,new_y)
    def __eq__(self,other):
        if self.x == other.x and self.y == other.y:
            return True
        return False
    
# p1 = Point(1,2)    
# p2 = Point(1,2)    
# print(p1 == p2) # True
# p3 = Point(11,2) 
# print(p2 == p3) # False

class Fu:
    def __init__(self,*args,**kwargs):
        print("init....,args,kwargs")
        print(self)

    def __new__(cls,*args,**kwargs):     
        print("new...,args,kwargs")
        obj = super().__new__(cls)
        print(obj)
        return obj

# Fu("a",x=10)     

# class inch(float):
#     # 错误的方式
#     def __init__(self, arg):
#        return  float.__init__(arg*0.0254)     

# print(inch(12))      

class inch(float):
    def __new__(cls, arg):
        return float.__new__(cls,arg*0.0254)
    
# print(inch(12.0))  

# 单例模式 也是通过__new__方法来创建
class Singleton:
    def __new__(cls,*args,**kwargs):
        it = cls.__dict__.get("__it__")
        if it is not None:
            return it
        cls.__it__ = it = super().__new__(cls)
        it.__init__(args,kwargs)
        return it
    def __init__(self,*agrs,**kwargs):
        pass

# c1 = Singleton()    
# print(c1)  #<__main__.Singleton object at 0x0000020F20CF61D0>
# c2 = Singleton()    
# print(c2)  #<__main__.Singleton object at 0x0000020F20CF61D0>

# minin is incomplete class,only have one method,no __init__ method
import json

class JsonMixin: # the mixin class only allowed to have one method
    def to_json(self):
        return json.dumps(self.__dict__)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age    

    def intr(self):
        print(f"Hello,My name is {self.name} and i am {self.age} years old...")    

class Student(JsonMixin,Person):
    def __init__(self, name, age,grade):
        super().__init__(name, age)
        self.grade = grade

stu = Student("Jackline",20,"High School")        
print(stu.to_json())
stu.intr()

# meta class, a class is used to create another class
# it defines how we should create a certain class
class UpperAttrMetaclass(type):
    # clsname: 类名, bases: 父类元组, dct: 类的属性字典
    def __new__(cls, clsname, bases, dct):
        # 筛选出不是以双下划线开头的属性名
        uppercase_attr = {}
        for name, val in dct.items():
            if name[0].isalpha():
                uppercase_attr[name.upper()] = val # 如果是以字母开头，就把这个属性改为大写
            else:
                uppercase_attr[name] = val
        
        # 调用 type 的 __new__ 来完成类的实际创建
        return super().__new__(cls, clsname, bases, uppercase_attr) # 关键，用新字典代替就字典，否则无效

class Test(metaclass=UpperAttrMetaclass):
    foo='hello' 
    __hi__ = "hi,sweetie"

# print(hasattr(Test,'foo'))   #False 
# print(hasattr(Test,'FOO'))   #True  
# print(Test.__dict__)  # {'__module__': '__main__', 'FOO': 'hello', '__hi__': 'hi,sweetie', '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None}
# print(hasattr(Test,"__hi__")) 

import threading
# 利用metaclass 类来实现singleton
class SingletonMeta(type):
    def __init__(cls,*args,**kwargs):
        cls.__instance = None
        cls.__lock = threading.RLock()
        super().__init__(*args,**kwargs)

    def __call__(cls,*args,**kwargs):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super.__call__(*args,**kwargs)    
        return cls.__instance        
    
class Boss(metaclass=SingletonMeta):
    pass

b1 = Boss()
b2 = Boss()
print(id(b1)) #2253173114304
print(id(b2)) #2253173114304

# 可插拔的哈希算法
class HashUtil:
    def __init__(self,algo,size=4096):
        self.algo = algo.lower()
        self.size = size
        self.harsher = getattr(__import__('hashlib'),algo.lower())()

    def __call__(self,stream):
        return self.to_hex_digest(stream)    
    
    def to_hex_digest(self,stream):  
        for buf in iter(lambda:stream.read(self.size),b''):
            self.harsher.update(buf)
        return self.harsher.hexdigest()
hash = HashUtil("sha1")

with open("./test.zip",'rb') as stream:
     print(hash(stream))   

# 迭代器和生成器
# 需要实现__iter__和__next__方法
class Feb:
    def __init__(self,num):
        self.num = num
        self.idx = 0
        self.a,self.b = 0,1

    def __iter__(self):
        return self
             
    def __next__(self):
        if self.idx < self.num:
            self.a,self.b = self.b,self.a+self.b         
            self.idx += 1
            return self.a    
        raise StopIteration()
    


# 多线程编程
import threading
import glob
import os
from PIL import Image
PREFIX = 'thumbnails'

def gen_thumdnail(infile,size,format='png'):
    if not os.path.exists(PREFIX):
        os.mkdir(PREFIX)
    file,ext = os.path.splitext(infile)
    file = file[file.rfind('/')+1:] # 获取纯文件名，去掉路径和扩展名
    # print(file)
    img = Image.open(infile)
    # print(img)
    img.thumbnail(size, Image.Resampling.LANCZOS)
    save_path = f'{PREFIX}/{file}_{size[0]}_{size[1]}{ext}'
    print(save_path)  
    img.save(save_path)    

# gen_thumdnail("./images/cuteg7.png",(32,32))    

def multi_thread_gen_thumdnail():
    if not os.path.exists(PREFIX):
        os.mkdir(PREFIX)
    for infile in glob.glob("./images/*.png"): # 大坑，用glob.glob变量的路径是./xxx\xxx.png的格式，需要统一路径，否则有问题
        infile = infile.replace('\\','/') # # ./images\cutesexy4.png，统一路径把 ./xxx\xxx.png变为./xxx/xxx.png
        for size in (16,32,48,64):
            threading.Thread(
                target=gen_thumdnail,
                args=(infile,(size,size))
            ).start()

# multi_thread_gen_thumdnail()

import time
from concurrent.futures import ThreadPoolExecutor

class Account:
    def __init__(self):
        self.balance = 0.0
        self.lock = threading.Lock()

    def deposit(self,amt):
        self.balance += amt
        time.sleep(0.001)   

def testThreadPool():
    acc = Account()
    futures = []
    pool = ThreadPoolExecutor(max_workers=10)        
    for _ in range(100):
        future = pool.submit(acc.deposit,10)
        futures.append(future)
    pool.shutdown()
    for f in futures:
        f.result()   
    print(acc.balance)    

# testThreadPool()
  
def testThreadPool():
    futures = []
    pool = ThreadPoolExecutor(max_workers=5)  
    if not os.path.exists(PREFIX):
        os.mkdir(PREFIX)
    for infile in glob.glob("./images/*.png"): # 大坑，用glob.glob变量的路径是./xxx\xxx.png的格式，需要统一路径，否则有问题
        infile = infile.replace('\\','/') # # ./images\cutesexy4.png，统一路径把 ./xxx\xxx.png变为./xxx/xxx.png
        for size in (16,32,48,64):
            future = pool.submit(gen_thumdnail,infile,(size,size))
            futures.append(future)

    for f in futures:
        f.result()     

# testThreadPool()           

from concurrent.futures import ProcessPoolExecutor
import time

def testProcessPool():
    with ProcessPoolExecutor() as excutor:
        if not os.path.exists(PREFIX):
            os.mkdir(PREFIX)  
        futures = []      
        for infile in glob.glob("./images/*.png"): # 大坑，用glob.glob变量的路径是./xxx\xxx.png的格式，需要统一路径，否则有问题
            infile = infile.replace('\\','/') # # ./images\cutesexy4.png，统一路径把 ./xxx\xxx.png变为./xxx/xxx.png
            for size in (16,32,48,64):
                result = excutor.submit(gen_thumdnail,infile,(size,size))
                futures.append(result)
    for f in futures:
        f.result()

if __name__ == '__main__':
    testProcessPool()

