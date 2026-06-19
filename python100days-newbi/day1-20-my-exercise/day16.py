"""high grade function"""

def calc(*args,**kwargs):
    items = list(args) + list(kwargs.values())
    result = 0
    for item in items:
        if type(item) in [int,float]:
            result += item
    return result
# be careful the usage,if you don;t use properly,you don't get the right result
# print(calc(*[1,2,3],**{"a":10.5,"b":20.2,"c":30.3}))  # 67     
# print(calc(1,2,3,a=10.5,b=20.2,c=30.3)) # # 67   

# extend fuction
def calc2(init_val,op,*args,**kwargs):
     items = list(args) + list(kwargs.values())
     result = init_val
     for item in items:
        if type(item) in [int,float]:
            result = op(result,item)
     return result       
def add(a,b):
    return a+b

def mul(a,b):
    return a * b

def sub(a,b):
    return a - b

def div(a,b):
    if b!=0:
        return a/b
    else:
        return -1
    
nms = [10,20,30]
dic = {"a":100,"b":200,"c":300}    
# print(calc2(0,sub,*nms,**dic))
# print(calc2(1,mul,*nms,**dic))
# print(calc2(1,add,*nms,**dic))
# print(calc2(1,div,*nms,**dic))

# python built in high grade func
# filter => filter(fuciton that return a boolean value,iterable) or net work as what you think
nums = [1,2,3,4,5,6,7,8,9,10]
evens = filter(lambda x: x%2==0,nums)
print(list(evens))
# map(function return no boolean result,iterable)
square = map(lambda x:x**2,nums)
print(list(square))

def is_prime_num(num): # ok
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True   

prime_nums = filter(is_prime_num,nums)
print(list(prime_nums)) # [1, 2, 3, 5, 7]