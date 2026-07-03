"""list2"""
#1
# languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript','Python','Python']
# languages.remove('Python') # just remove one item at a time. if you trying to remove an item that not exists,will cause exception
# if 'SQL' in languages:
#     languages.remove('SQL')
# print(languages)
#2
# items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
# print(items.index('Python')) # 0  find the first one,if an item you are looking for not exists,will cause exception
# print(items.count('Python')) # 2

# # sort=>get sequence, no return value, reverse->turn it back way,no return value
# items.sort()
# print(items) # ['C++', 'Java', 'Java', 'Kotlin', 'Python', 'Python']
# items.reverse()
# print(items) # ['Python', 'Python', 'Kotlin', 'Java', 'Java', 'C++']
#3 list comprehension
arr = [i for i in range(31) if i%2==0]
print(arr) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

# 4 list inside list
# scores = [[95, 83, 92], [80, 75, 82], [92, 97, 90], [80, 78, 69], [65, 66, 89]]
# print(scores[1]) # [80, 75, 82]
# print(scores[1][0]) # 80
# for score in scores:
#     for s in score:
#         print(s,end=" ")
#     print()

# 5.Chinese lottery demo, 6redball + 1blue ball
# import random
# red_balls = [i for i in range(1,34)]
# selected_redballs = []
# for _ in range(6):
#     index = random.randrange(len(red_balls))
#     selected_redballs.append(red_balls.pop(index))
# selected_redballs.sort()    
# # print(f"red balls:{selected_reballs}")   
# for ball in selected_redballs:
#     print(f'\033[031m{ball:0>2d}\033[0m', end=' ') # output red color
# blue_ball = random.randrange(1,17)
# # print(f"blue all:{blue_ball}")
# print(f'\033[034m{blue_ball:0>2d}\033[0m') # output blue color
    
# 6.写法2
import random

red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]
# 从红色球列表中随机抽出6个红色球（无放回抽样）
selected_balls = random.sample(red_balls, 6)
# 对选中的红色球排序
selected_balls.sort()
# 输出选中的红色球
for ball in selected_balls:
    print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
# 从蓝色球列表中随机抽出1个蓝色球
blue_ball = random.choice(blue_balls)
# 输出选中的蓝色球
print(f'\033[034m{blue_ball:0>2d}\033[0m')