def match_user_qq():
    import re

    username = input("Please enter user name:")
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$',username)
    if not m1:
        print("not valid,Please enter valid user name...")
    qq = input("Please enter qq:")
    m2 = re.match(r'^[1-9]\d{4,11}$',qq)    
    if not m2:
        print("Invalid qq,please enter valid qq")
    if m1 and m2:
        print("Both username and qq are correct!!")

# 方法一：查找所有匹配并保存到一个列表中
def get_tel():
    import re
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    txt = '''重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
不是15600998765，也不是110或119，王大锤的手机号才是15600998765。'''
    tels = re.findall(pattern,txt)
    for tel in tels:
        print(tel)

# get_tel()
"""
13512346789
15600998765
15600998765
"""

# 方法二：通过迭代器取出匹配对象并获得匹配的内容
def get_tel2():
    import re
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    txt = '''重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
不是15600998765，也不是110或119，王大锤的手机号才是15600998765。'''
    for tem in pattern.finditer(txt):
        print(tem.group())

# get_tel2()
# 方法三：通过search函数指定搜索位置找出所有匹配 
def get_tel3():
    import re
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    txt = '''重要的事情说8130123456789遍，我的手机号是13512346789这个靓号,不是15600998765,也不是110或119,王大锤的手机号才是15600998765。'''
    m = pattern.search(txt)
    while m:
        print(m.group())
        m = pattern.search(txt,m.end())

# get_tel3()

# ：替换字符串中的不良内容
def repl_bad():
    import re
    tst = "Oh, shit! 你是傻逼吗? Fuck you.呵呵，操你妈"
    # good = re.sub('fuck|shit|[傻逼肏][操比笔逼叉缺吊碉雕]','*',tst,flags=re.IGNORECASE) # 不好
    good = re.sub('fuck|shit|[傻逼肏]|[操比笔逼叉缺吊碉雕]','*',tst,flags=re.IGNORECASE) # 好
    # good = re.sub('fuck|shit|[傻逼肏操比笔逼叉缺吊碉雕]','*',tst,flags=re.IGNORECASE) # 好
    print(good)

# repl_bad()    

# 拆分长字符串
import re

poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
sentences_list = re.split(r'[，。]', poem)
sentences_list = [sentence for sentence in sentences_list if sentence]
for sentence in sentences_list:
    print(sentence)