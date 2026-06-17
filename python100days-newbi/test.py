from day14 import factorial,factorial2

# print(factorial(5))
print(factorial2(5))

# / = > force the fuction use posrtional params
def is_triangle(a,b,c,/):
    return a+b > c and b+c > a and a+c > b

# print(is_triangle(1,2,3))  # False
# print(is_triangle(a=3,b=4,c=5)) # TypeError: is_triangle() got some positional-only arguments passed as keyword arguments: 'a, b, c'

def test(a,b,/,c): # / means the arguments before / have to be positional after / don't has to be positional
    return a+b -c
# print(test(1,4,3))
print(test(1,4,c=3))
