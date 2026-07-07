# 1.custom function,syntax


```python
"""
define a funtion:
def function name(parameters or nothing):
    code
    return or no return
"""
```


```python
"""create a function with no params and no return value"""
# def my_function():
#   print("Hello from a function")
# def greeting():
#     print("Welcome to my live show")
    
# greeting()    
```

    Welcome to my live show
    


```python
"""
create a function with param but no return value:
def eat(food):
    print("I am eating" + food)
"""
# def lunch(food):
#     print("Hello ,I am eating "+food)
    
# lunch("Cake")    
    
```

    Hello ,I am eating Cake
    


```python
"""
create a function with no param but has return value:
def getNum():
   return 100
"""
# def gen_num():
#     return 100
# num = gen_num()
# print("num=" , num)
```

    num= 100
    


```python
"""
create a function with param and has return value:
def doubleUp(x):
   return x*2
"""
# def triple_up(x):
#     return x *3 
# print(triple_up(5))
```

    15
    


```python
"""
create Arbitrary Arguments, *args
def show_max(*args):
    biggest = args[0]
    for x in args:
        if x > biggest:
            biggest = x
    return biggest    
"""

# def show_max(*args):
#     biggest = args[0]
#     for x in args:
#         if x > biggest:
#             biggest = x
#     return biggest   
# show_max(1,2,3,4,5)

def get_max_val(*nums):
    maxVal = nums[0]
    for x in nums:
        if x > maxVal:
            maxVal = x

    return maxVal

numbers = [10,5,50,100]
ret = get_max_val(*numbers)  # need unpack
print("The Max Value is:",ret)
```

    The Max Value is: 100
    


```python

```


```python
"""
Keyword Arguments
You can also send arguments with the key = value syntax.
This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


"""
# def info(c1,c2,c3):
#     print("The youngest one is " ,c3)
    
# info(c3=10,c1=20,c2=30)    

```

    The youngest one is  10
    


```python
# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
"""
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

"""

# def get_last_name(**name):
#     print("The last name is",name["last"])
    
# get_last_name(fname="Jack",last="Daniel")    
```

    The last name is Daniel
    


```python
# Default Parameter Value
# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:
"""
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

"""
# def showCountry(country="China"):
#     print("My Country is ",country)
    
# showCountry()
# showCountry("Norway")


```

    My Country is  China
    My Country is  Norway
    


```python
# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
"""
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

"""
# def output(items):
#     for x in items:
#         print(x)
        
# output([10,20,30])        
```

    10
    20
    30
    


```python
# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
"""
def myfunction():
  pass

"""
def nothing():
    pass
    
nothing()
```

 ## only valid in python3.8 and up


```python
# Positional-Only Arguments  python 3.8
# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments:
"""
def my_function(x):
  print(x)

my_function(x = 3)

"""
# def demo(x):
#     print("The number is:",x)
    
# demo(x=50)    

"""
def my_function(x,/): 
  print(x)

my_function(x = 3) # error

"""
# def demo(x, /):
#     print("The number is:",x)
    
# demo(50)    
```




    '\ndef my_function(x,/): \n  print(x)\n\nmy_function(x = 3) # error\n\n'



# 2.Python Built-in functions


```python
# abs()
"""
Definition and Usage
The abs() function returns the absolute value of the specified number.

Syntax
abs(n)
"""
# print(abs(-10))
```

    10
    


```python
# all()
"""
Definition and Usage
The all() function returns True if all items in an iterable are true, otherwise it returns False.

If the iterable object is empty, the all() function also returns True.
ex:
mylist = [True, True, True]
x = all(mylist)
"""
# rets = [True,True,True]
# print(all(rets))
```




    '\nDefinition and Usage\nThe all() function returns True if all items in an iterable are true, otherwise it returns False.\n\nIf the iterable object is empty, the all() function also returns True.\nex:\nmylist = [True, True, True]\nx = all(mylist)\n'




```python
# any()
# Definition and Usage
# The any() function returns True if any item in an iterable are true, otherwise it returns False.

# If the iterable object is empty, the any() function will return False.

# Syntax
# any(iterable)

"""
mylist = [False, True, False]
x = any(mylist)
"""
# data = [False, True, False]
# print(any(data))
```

    True
    


```python
# ascii()
# Definition and Usage
# The ascii() function returns a readable version of any object (Strings, Tuples, Lists, etc).

# The ascii() function will replace any non-ascii characters with escape characters:

# å will be replaced with \xe5.

"""
Example
Escape non-ascii characters:

x = ascii("My name is Ståle")
"""

o = {"name":"jack"}
print(ascii(o))    

ascii("My name is Ståle")
```

    {'name': 'jack'}
    




    "'My name is St\\xe5le'"




```python
# bin(n)
# Definition and Usage
# The bin() function returns the binary version of a specified integer.

# The result will always start with the prefix 0b.

# Syntax
# bin(n)
"""
x = bin(36)
"""
# bin(3)
```




    '0b11'




```python
# chr()
# Definition and Usage
# The chr() function returns the character that represents the specified unicode.

# Syntax
# chr(number)

# x = chr(97)
# print(chr(65))
```

    A
    


```python
# dir()
# Definition and Usage
# The dir() function returns all properties and methods of the specified object, without the values.

# This function will return all the properties and methods, even built-in properties which are default for all object.

# person={"name":"John","age":10}

# dir(person)
# jade = {"name":"Jade","age":18}
# print(dir(jade))
```

    ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
    


```python
# divmod()
# Definition and Usage
# The divmod() function returns a tuple containing the quotient  and the remainder when argument1 (dividend) is divided by argument2 (divisor).

# Syntax
# divmod(dividend, divisor)
# x = divmod(5, 2)
# print(divmod(10,3))

```

    (3, 1)
    


```python
# enumerate()
# Definition and Usage
# The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.

# The enumerate() function adds a counter as the key of the enumerate object.
# Convert a tuple into an enumerate object:

# x = ('apple', 'banana', 'cherry')
# y = enumerate(x)
# x = [1,2,3]
# y = enumerate(x)
# print(tuple(y))
```

    ((0, 1), (1, 2), (2, 3))
    


```python
# eval()
# Definition and Usage
# The eval() function evaluates the specified expression, if the expression is a legal Python statement, it will be executed.

# Syntax
# eval(expression, globals, locals)
# example1:
# print(eval('1+2'))
# print(eval("sum([1, 2, 3, 4])"))
#test1
# print(eval("2**2"))

# example2: write an express of the var and pass the value of var then the function get back the result
# def function_creator():

#     # expression to be evaluated
#     expr = input("Enter the function(in terms of x):")

#     # variable used in expression
#     x = int(input("Enter the value of x:"))

#     # evaluating expression
#     y = eval(expr)

#     # printing evaluated result
#     print("y =", y)



# function_creator()
# test2:
# def do_it():
#     expr = input("Enter function for x:")
#     x = int(input("Please enter the value for x:"))
#     y = eval(expr)
#     print("The result:",y)
            
# do_it()

# example3:
# expression = 'x*(x+1)*(x+2)'
# print(expression)

# x = 3

# result = eval(expression)
# print(result)
# test3:
# exp = "x+x*4"
# x = 3
# print(eval(exp))

# example4:
# x = 5
# print(eval('x == 4'))
# a = 20
# print(eval("a==10"))

# x = None
# print(eval('x is None'))
# test4:
# b = None
# print(eval("b is None")) # 
```

## 上一次直播结束位置


```python
# exec()
# Definition and Usage
# The exec() function executes the specified Python code.

# The exec() function accepts large blocks of code, unlike the eval() function which only accepts a single expression

# Syntax
# exec(object, globals, locals)

# ex1:
# x = 'name = "John"\nprint(name)'
# exec(x)
#test1:
# str = 'name="Benny"\nprint(name)'
# exec(str)

# ex2:

# prog = 'print("The sum of 5 and 10 is", (5+10))'
# exec(prog)
# test2:
# proc = "print('The sum of 10 and 15 is',(10+15))"
# exec(proc)

# ex3:
# exec("print(dir())", {"built" : __builtins__}, {"sum": sum, "iter": iter})
# test3:
exec("print(dir())",{"name":"jack"},{"age":30})
    

```

    ['age']
    


```python
# filter() this is a hi-grade function,it need a function as the first param,and then ,you pass the collect as data
# Definition and Usage
# The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.

# Syntax
# filter(function, iterable)
# ExampleGet your own Python Server
# Filter the array, and return a new array with only the values equal to or above 18:

# ages = [5, 12, 17, 18, 24, 32]

# def myFunc(x):
#   if x < 18:
#     return False
#   else:
#     return True

# adults = filter(myFunc, ages)

# for x in adults:
#   print(x)
# test1:

# def filter_func(x):
#     if x >= 18:
#         return True
#     else:
#         return False
    
# ages = [20,30,15,35,60]
# rets = filter(filter_func,ages)
# print(list(rets))
    


    
```

    [20, 30, 35, 60]
    


```python
# help(),this function can provide infomations about the python 
# ex1,to see the python built-in modules: 
# help('modules')

# ex2,to see the list class in python:
# help('list')
    
```


```python
# hex()
# ExampleGet your own Python Server

# Definition and Usage
# The hex() function converts the specified number into a hexadecimal value.

# The returned string always starts with the prefix 0x.
# Convert 255 into hexadecimal value:

# x = hex(255)
# test:
# print(hex(100))
```

    0x64
    


```python
# id()
# Definition and Usage
# The id() function returns a unique id for the specified object.

# All objects in Python has its own unique id.

# The id is assigned to the object when it is created.

# The id is the object's memory address, and will be different for each time you run the program. 
# (except for some object that has a constant unique id, like integers from -5 to 256 in some versions of Python).

# ExampleGet your own Python Server
# Return the unique id of a tuple object:

# x = ('apple', 'banana', 'cherry')
# y = id(x)  # every time different

# test:
# obj = {"name":"Kenny","age":30}
# print(id(obj))

```

    3253902137168
    


```python
# input()
# Definition and Usage
# The input() function allows user input.

# Syntax
# input(prompt)
# Example
# Ask for the user's name and print it:

# print('Enter your name:')
# x = input()
# print('Hello, ' + x)
# test:
# n = input("Enter you name:")
# print(f"Hello {n},How is your day?")

```

    Enter you name: Kenny
    

    Hello Kenny,How is your day?
    


```python
# isinstance()
# Definition and Usage
# The isinstance() function returns True if the specified object is of the specified type, otherwise False.

# If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.

# Syntax
# isinstance(object, type)

# Example1
# Check if the number 5 is an integer:

# x = isinstance(5, int)
# print(x)
# test1:
# print(isinstance(100.0,float)) # Ture

# example2: # be careful of the usage
# x = isinstance("Hello", (float, int, str, list, dict, tuple))
# print(x)
# print(isinstance(10,(int,float,str,list,dict)))  #True


    
```

    True
    


```python
# inter() not very important

# Definition and Usage
# The iter() function returns an iterator object.

# Syntax
# iter(object, sentinel)

# Example
# Create an iterator object, and print the items:

# x = iter(["apple", "banana", "cherry"])
# print(next(x))
# print(next(x))
# print(next(x))

```

    apple
    banana
    cherry
    


```python
# len()

# Definition and Usage
# The len() function returns the number of items in an object.

# When the object is a string, the len() function returns the number of characters in the string.

# Syntax
# len(object)

# Example
# Return the number of items in a list:

# mylist = ["apple", "banana", "cherry"]
# x = len(mylist)
# test:
# print(len("Hello World")) #11
# print(len([1,2,3,4,5,6,7,8,9])) # 9

```

    9
    


```python
# map() map is a hi-grade function,it needs a function as the first parameter,and a collection as data
# Definition and Usage
# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

# Syntax
# map(function, iterables) returns a generator object that can be converted into a list or set or tuple

# Example
# Calculate the length of each word in the tuple:

# def myfunc(n):
#   return len(n)

# x = map(myfunc, ('apple', 'banana', 'cherry'))
# print(list(x))
# test1:

# def doubl_up(x):
#     return 2*x
# print(list(map(doubl_up,[1,2,3])))

# Example2
# Make new fruits by sending two iterable objects into the function:

# def myfunc(a, b):
#   return a + b

# list(map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple')))

# test2:
# def joinup(a,b):
#     return a+b
# ret = list(map(joinup,("Jack:","Mary:","Jean:"),("100","70","80")))
# print(ret)
   

```

    ['Jack:100', 'Mary:70', 'Jean:80']
    


```python
# max() gets the biggest one and min() gets the smallest one
# Definition and Usage
# The max() function returns the item with the highest value, or the item with the highest value in an iterable.

# If the values are strings, an alphabetically comparison is done.

# Syntax
# max(n1, n2, n3, ...)
# Or:
# max(iterable)
# Example
# Return the largest number:

# x = max(5, 10)
# print("biggest value:",x)
# y = min(5,10)
# print("smallest value:",y)
# test:

# use collection
# print(max((1,2,3,4,5)))
# test2:
# print(max(100,550,1000))
# nm=[10,20,5,30,15,35]
# print(max(nm))
# print(min(nm))
    
```


```python
# oct()
# Definition and Usage
# The oct() function converts an integer into an octal string.

# Octal strings in Python are prefixed with 0o.

# Syntax
# oct(int)
# Example
# Convert the number 12 into an octal value:

# oct(12)

# test: 
# print(oct(10))

```

    0o12
    


```python
# open()
# Definition and Usage
# The open() function opens a file, and returns it as a file object.

# Read more about file handling in our chapters about File Handling.

# Syntax
# open(file, mode)

# Parameter Values
# Parameter	Description
# file	The path and name of the file
# mode	A string, define which mode you want to open the file in:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exist

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)


# f = open("demo.txt", "r")
# print(f.read())

# test:
# f = open("wc.txt","r")
# print(f.read())

```


```python
# ord()
# Definition and Usage
# The ord() function returns the number representing the unicode code of a specified character.

# Syntax
# ord(character)

# ord("h")
# test:
# print(ord("A")) # 65


```

    65
    


```python
# pow()

# Definition and Usage
# The pow() function returns the value of x to the power of y (xy).

# If a third parameter is present, it returns x to the power of y, modulus z.

# Syntax
# pow(x, y, z)
# Parameter Values
# Parameter	Description
# x	A number, the base
# y	A number, the exponent
# z	Optional. A number, the modulus

# Example
# Return the value of 4 to the power of 3 (same as 4 * 4 * 4):

# x = pow(4, 3)
# print(x)
# test:
# print(pow(2,3))

```

    8
    


```python
# print()
# Definition and Usage
# The print() function prints the specified message to the screen, or other standard output device.

# The message can be a string, or any other object, the object will be converted into a string before written to the screen.

# Syntax
# print(object(s), sep=separator, end=end, file=file, flush=flush)
# Parameter Values
# Parameter	Description
# object(s)	Any object, and as many as you like. Will be converted to string before printed
# sep='separator'	Optional. Specify how to separate the objects, if there is more than one. Default is ' '
# end='end'	Optional. Specify what to print at the end. Default is '\n' (line feed)
# file	Optional. An object with a write method. Default is sys.stdout
# flush	Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False

# Example
# Print a message onto the screen:

# print("Hello World")
# test:    
# print("Hello,everyone")

```

    Hello,everyone
    


```python
# range() this function is used inside a for loop to control the loop times
# Definition and Usage
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

# Syntax
# range(start, stop, step)
# Parameter Values
# Parameter	Description
# start	Optional. An integer number specifying at which position to start. Default is 0
# stop	Required. An integer number specifying at which position to stop (not included).
# step	Optional. An integer number specifying the incrementation. Default is 1

# Example
# Create a sequence of numbers from 0 to 5, and print each item in the sequence:

# x = range(6)
# for n in x:
#   print(n)

# test:
# for x in range(6):
#     print(x+1)
```

    1
    2
    3
    4
    5
    6
    


```python
# repr()	Returns a readable version of an object
# # example1:

# s = 'RUNOOB'
# repr(s)

# # example2:
# dict = {'runoob': 'runoob.com', 'google': 'google.com'};
# repr(dict)

    
```




    "{'runoob': 'runoob.com', 'google': 'google.com'}"




```python
# reversed()
# Definition and Usage
# The reversed() function returns a reversed iterator object.

# Syntax
# reversed(sequence)
# Parameter Values
# Parameter	Description
# sequence	Required. Any iterable object

# Example
# Reverse the sequence of a list, and print each item:

# alph = ["a", "b", "c", "d"]
# ralph = reversed(alph)
# for x in ralph:
#   print(x)
# test:
# nums = [5,4,3,2,1]
# rev_nums = reversed(nums)
# print(list(rev_nums))


```

    [1, 2, 3, 4, 5]
    


```python
# round()
# Definition and Usage
# The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.

# The default number of decimals is 0, meaning that the function will return the nearest integer.

# Syntax
# round(number, digits)
# Parameter Values
# Parameter	Description
# number	Required. The number to be rounded
# digits	Optional. The number of decimals to use when rounding the number. Default is 0

# Example
# Round a number to only two decimals:

# x = round(5.76543, 2)
# print(x)
# test:
# print(round(4.45)) # 4
# print(round(4.45,1)) # 4.5
```

    4.5
    


```python
# sorted()
# Definition and Usage
# The sorted() function returns a sorted list of the specified iterable object.

# You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.

# Note: You cannot sort a list that contains BOTH string values AND numeric values.

# Syntax
# sorted(iterable, key=key, reverse=reverse)
# Parameter Values
# Parameter	Description
# iterable	Required. The sequence to sort, list, dictionary, tuple etc.
# key	Optional. A Function to execute to decide the order. Default is None
# reverse	Optional. A Boolean. False will sort ascending, True will sort descending. Default is False

# Example
# Sort a tuple:

# a = ("b", "g", "a", "d", "f", "c", "h", "e")
# x = sorted(a)
# print(x)
# test:
# a = [10,5,4,12,7,8]
# ret = sorted(a, reverse=True)
# print(ret)


```

    [12, 10, 8, 7, 5, 4]
    


```python
# sum()
# Definition and Usage
# The sum() function returns a number, the sum of all items in an iterable.

# Syntax
# sum(iterable, start) start represent the init value of the total
# Parameter Values
# Parameter	Description
# iterable	Required. The sequence to sum
# start	Optional. A value that is added to the return value

# a = (1, 2, 3, 4, 5)
# sum(a, 7)
# test:
# n = [1,2,3,4]
# print(sum(n,10))


```

    20
    


```python
# type()
# Definition and Usage
# The type() function returns the type of the specified object

# Syntax
# type(object, bases, dict)
# Parameter Values
# Parameter	Description
# object	Required. If only one parameter is specified, the type() function returns the type of this object
# bases	Optional. Specifies the base classes
# dict	Optional. Specifies the namespace with the definition for the class

# Example
# Return the type of these objects:

# a = ('apple', 'banana', 'cherry')
# b = "Hello World"
# c = 33

# print(type(a))
# print(type(b))
# print(type(c))
# test:
# print(type(10))
print(type("hello"))

```

    <class 'str'>
    


```python
# zip()
# Definition and Usage
# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.

# If the passed iterables have different lengths, the iterable with the least items decides the length of the new iterator.

# Syntax
# zip(iterator1, iterator2, iterator3 ...)
# Parameter Values
# Parameter	Description
# iterable1, iterable2, iterable3 ...

# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica")

# x = zip(a, b)
# print(tuple(x))

# test:
names = ["May","kenny","jade"]
scores = [80,100,70]
print(list(zip(names,scores)))

```

    [('May', 80), ('kenny', 100), ('jade', 70)]
    


```python

```
