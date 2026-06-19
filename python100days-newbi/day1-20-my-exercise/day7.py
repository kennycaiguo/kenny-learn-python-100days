"""
febonacci
"""

# a,b = 0,1
# for _ in range(20):
#     a,b = b,a+b
#     print(a,end=",")


# # narcissistic number
# for num in range(100,1000):
#     low = num % 10
#     mid = num //10%10
#     high = num //100
#     if low**3 + mid **3 + high **3 == num:
#         print(num,end=",") # 153,370,371,407,

# reversed a number
# num = int(input("input a number that is greater than 0 >>>"))
# print(f"you enter: {num}")
# rev = 0
# while num > 0:
#     rev = rev * 10 + num % 10
#     num //= 10
# print(f"the reved num is {rev}")    

#100$ buy 100chicken 
# for x in range(0,21):
#     for y in range(0,34):
#         for z in range(0,100,3):
#             if x+y+z == 100 and 5*x + 3*y + z//3 ==100:
#                 print(f"Rooster:{x},hen:{y},Little chicken{z}") # 4 way to do

#100$ buy 100chicken  solution 2 z = 100 - x-y

# for x in range(0,21):
#     for y in range(0,34):
#         z = 100 -x-y
#         if  z % 3 == 0 and 5*x + 3*y + z//3 ==100:
#             print(f"Rooster:{x},hen:{y},Little chicken{z}") # 4 way to do

"""
Craps赌博游戏

Version: 1.0
Author: 骆昊
"""
import random

money = 1000
while money > 0:
    print(f'你的总资产为: {money}元')
    # 下注金额必须大于0且小于等于玩家的总资产
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break
    # 用两个1到6均匀分布的随机数相加模拟摇两颗色子得到的点数
    first_point = random.randrange(1, 7) + random.randrange(1, 7)
    print(f'\n玩家摇出了{first_point}点')
    if first_point == 7 or first_point == 11:
        print('玩家胜!\n')
        money += debt
    elif first_point == 2 or first_point == 3 or first_point == 12:
        print('庄家胜!\n')
        money -= debt
    else:
        # 如果第一次摇色子没有分出胜负，玩家需要重新摇色子
        while True:
            current_point = random.randrange(1, 7) + random.randrange(1, 7)
            print(f'玩家摇出了{current_point}点')
            if current_point == 7:
                print('庄家胜!\n')
                money -= debt
                break
            elif current_point == first_point:
                print('玩家胜!\n')
                money += debt
                break
print('你破产了, 游戏结束!')
