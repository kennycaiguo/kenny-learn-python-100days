"""function practise"""

import random
import string

all_chars = string.digits + string.ascii_letters
def gen_code(all_chars,len=4): # works
    ver_codes =[]
    for i in range(len):
        ver_codes.append(random.choice(all_chars))
    return "".join(ver_codes)

# print(gen_code(all_chars,4))
# get prime number,only can dived by 1 and itself num**0.5 -> square root
def is_prime_num(num): # ok
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True    

# print(is_prime_num(3))

def get_prime(num): # ok
    primes = []
    for i in range(1,num+1):
        if is_prime_num(i):
            primes.append(i)
    return primes
# print(get_prime(100))

# Greatest Common Divisor gcd(x,y)*lcm(x,y) = x*y => lcm(x,y)=x*y //gcd(x,y)
def get_gcd(x,y):
    while y % x != 0:
        x,y = y%x,x
    return x    

# print(get_gcd(12,18))

def get_lcm(x,y):
    return x*y //get_gcd(x,y)

print(get_lcm(12,18))


def ptp(data):
    """极差（全距）"""
    return max(data) - min(data)


def mean(data):
    """算术平均"""
    return sum(data) / len(data)


def median(data):
    """中位数"""
    temp, size = sorted(data), len(data)
    if size % 2 != 0:
        return temp[size // 2 + 1]  # 注意，参考git repo 有错误！！！
    else:
        return mean(temp[size // 2 - 1:size // 2 + 1])
    
def var(data, ddof=1):
    """方差"""
    x_bar = mean(data)
    temp = [(num - x_bar) ** 2 for num in data]
    return sum(temp) / (len(temp) - ddof)

def std(data, ddof=1):
    """标准差"""
    return var(data, ddof) ** 0.5    

def cv(data, ddof=1):
    """变异系数"""
    return std(data, ddof) / mean(data)


def describe(data):
    """输出描述性统计信息"""
    print(f'均值: {mean(data)}')
    print(f'中位数: {median(data)}')
    print(f'极差: {ptp(data)}')
    print(f'方差: {var(data)}')
    print(f'标准差: {std(data)}')
    print(f'变异系数: {cv(data)}')