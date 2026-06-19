""""function and module"""
def factorial(x):
    if x==0 or x == 1:
        return 1
    return x * factorial(x-1)

def factorial2(x):
    fx = 1
    for i in range(1,x+1):
        fx *= i
    return fx    

if __name__ == "__main__":
    # # m!
    # fm = 1
    # for i in range(1,m+1):
    #     fm *=i

    # # n!
    # fn = 1
    # for i in range(1,n+1):
    #     fn *=i

    # # (m-n)!
    # k = m-n
    # fk = 1
    # for i in range(1,k+1):
    #     fk *= i      

    # # fm//fn//fk == fm//(fn*fk)
    # print(fm//(fn*fk))
    import math
    m = int(input("Enter the first number: "))
    n = int(input("Enter the first number: ")) 
    # print(factorial(m)//factorial(n)//factorial(m-n))
    print(math.factorial(m)//math.factorial(n)//math.factorial(m-n))
    