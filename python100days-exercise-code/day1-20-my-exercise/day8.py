"""
在开始本节课的内容之前，我们先给大家一个编程任务，将一颗色子掷 6000 次，统计每种点数出现的次数。
这个任务对大家来说应该是非常简单的，我们可以用 1 到 6 均匀分布的随机数来模拟掷色子，然后用 6 个变量分别记录每个点数出现的次数，
信通过前面的学习，大家都能比较顺利的写出下面的代码。
"""

import random

# f1 = f2 = f3 = f4 = f5 = f6 =0
# for _ in range(6000):
#     face = random.randint(1,7)
#     if face == 1:
#         f1 += 1
#     elif face ==2:
#         f2 += 1
#     elif face ==3:
#         f3 += 1
#     elif face ==4:
#         f4 += 1
#     elif face ==5:
#         f5 += 1
#     else: # here the last one else and elif different!!!,if use elif you lost almost 1000 times
#         f6 += 1
# print(f"1:{f1},2:{f2},3:{f3},4:{f4},5:{f5},6:{f6}")        

        
# use list 
counters = [0] * 6
print(counters) #[0, 0, 0, 0, 0, 0]
for _ in range(6000):
    face = random.randrange(1,7)
    counters[face-1] +=1
print(counters)    