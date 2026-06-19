"""tuple"""
# t = (1,2,3) 
# # len-> numer of element inside a tuple
# print(len(t))
# # indexing
# print(t[1]) # 2
# # slicing
# print(t[:2]) # (1, 2)
# print(t[1:]) # (2, 3)
# # a tuple is not changable
# # t[0] = 3 # TypeError: 'tuple' object does not support item assignment
# # print(t) 
# # use 2 tuples to create a new tuple
# t2 = t + (4,5)
# print(t2) # (1, 2, 3, 4, 5)
# # tuple with list element,the list itself allow to change
# t = (1,[2,3],4)
# t[1][0] = 10
# print(t) # (1, [10, 3], 4)
# t[1].append(5)
# print(t) # (1, [10, 3, 5], 4)
# t[1].pop()
# print(t) # (1, [10, 3], 4)
# # compare
# t = (1,2,3) 
# print(t == (1,2,3) ) # True
# print(t > (1,2)) # > means has more element,compare the len
# # el in tuple
# print(4 in t) # False
# for i in t:
#     print(i,end=" ") # 1 2 3 
# print()    
# # find
# print(t.index(3)) # the el 3 has a index 2
# # how to define a tuple that has only on element
# t = ()
# print(type(t)) # <class 'tuple'>  empty tuple
# t = (10)
# print(type(t)) # <class 'int'>
# t = (10,)
# print(type(t)) # <class 'tuple'>

# pack and unpack
a = 1,10,100,1000  # <class 'tuple'>
print(type(a))
print(*a) # 1 10 100 1000
# a tuple has 4 element,but we only provide 3 variable,fisrt->first var,second->second var , rest->third var,then third become a list
i,j,*k = a # the * is needed,or cause an exception
# i,j,k = a # error ValueError: too many values to unpack (expected 3)
print(i,j,k) # 1 10 [100, 1000]
*i,j,k = a # rule the var contains * will be the last one  to get value
print(i,j,k) #  [1,10],100,1000
# *i,*j,*k # not allow ,only one unpack sign (*) allowed 
# list,range,tuple,str are all allow to upack
a, b, *c = range(1, 10)
print(a, b, c) # h ['e', 'l', 'l'] o
a, b, c = [1, 10, 100]
print(a, b, c) # 1 10 100
a, *b, c = 'hello'
print(a, b, c) # h ['e', 'l', 'l'] o
# exchange value,only allow 2 or 3 variables
a,b = 10,20
print(a,b) #10 20
a,b = b,a
print(a,b) # 20 10
a,b,c,d = 1,2,3,4
a,b,c,d = d,c,b,a
print(a,b,c,d) # 4 3 2 1
a,b,c,d,e = 10,20,30,40,50
a,b,c,d,e = e,d,c,b,a
print(a,b,c,d,e) # 50 40 30 20 10
# type convert
# tuple -> list : list(tuple object)
print(list((11,22,33))) # [11, 22, 33]
# list->tuple: tuple(list object)
print(tuple(['a','b','c'])) # ('a', 'b', 'c')
