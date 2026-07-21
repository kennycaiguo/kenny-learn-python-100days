**分享66个Python管理系统源代码总有一个是你想要的**

 

源码下载链接：[https://pan.baidu.com/s/1FGmE9Q_NE1-cjjoxU540BQ?pwd=8888 ](https://pan.baidu.com/s/1FGmE9Q_NE1-cjjoxU540BQ?pwd=8888)

提取码：8888

项目名称

automobile-sales-management-system汽车销售管理系统 Python Vue

BNUZ教务系统认证爬虫Python语言实现，你可以用这个爬虫去模拟登录教务系统以检验学生账号是否合法

Book Managementsystem based on python QT.(基于Python QT的图书管理系统)

CRM管理系统 -- python

elasticsearch_python+flask检索系统

FZQOJ自动签到系统，基于python+selenium+javascript

JLU打卡系统（Python）

JXNU操作系统实验课程代码 -- Python版

mac系统下的appium环境搭建（python）

Mesoor 推荐系统 Python SDK

```
import os
import shutil
def void_folder(path):
    # 访问path路径下的文件或文件夹
    lst = os.listdir(path)
    # 打印每一层的文件或文件夹
    for name in lst:
        # 拼接名称，得到绝对路径，判断该文件是否符合是文件夹
        real_path = os.path.join(path, name)
        # 如果是文件夹，则打空格表示，并且递归访问下一层
        if os.path.isdir(real_path):
            # print(name)
            files = os.listdir(real_path)
            if len(files) == 0:
                print("void_folder()："+name)
                shutil.rmtree(real_path)
                endindex = len(real_path) - len(name)
                real_path = real_path[0:endindex]
                void_folder(real_path)
            else:
                void_folder(real_path)
        # 如果不是文件夹，直接打印，不再递归访问下一层
        else:
            #print(name)
            pass
def void_file(dirPath):
    dirs = os.listdir(dirPath)  # 查找该层文件夹下所有的文件及文件夹，返回列表
    for file in dirs:
        file_full_name = dirPath + '/' + file
        file_ext = os.path.splitext(file_full_name)[-1]
        if file_ext is None  or file_ext=="":
            continue
        if "rar" == str(file_ext.split(".")[1]):
            os.remove(file_full_name)
        if "zip" == str(file_ext.split(".")[1]):
            os.remove(file_full_name)
        if "gz" == str(file_ext.split(".")[1]):
            os.remove(file_full_name)
        if "tgz" == str(file_ext.split(".")[1]):
            os.remove(file_full_name)
# 查找指定文件夹下所有相同名称的文件
def search_file(dirPath, fileName):
    dirs = os.listdir(dirPath)  # 查找该层文件夹下所有的文件及文件夹，返回列表
    for currentFile in dirs:  # 遍历列表
        absPath = dirPath + '/' + currentFile
        if os.path.isdir(absPath):  # 如果是目录则递归，继续查找该目录下的文件
            search_file(absPath, fileName)
        elif currentFile == fileName:
            print(absPath)  # 文件存在，则打印该文件的绝对路径
            os.remove(absPath)
```

python ATM 和课程系统

Python Flask 构建基于微信小程序的订餐系统

Python Flask开源博客系统Blog_mini的修改版

python 内容管理系统

python 智能问答系统QA的数据处理

Python 简单调度系统

Python-Django-博客系统

python-flask框架基于爬虫实现简单的多语言翻译系统

python—客户管理系统

python仿优酷系统

python信息管理系统

python四六级报名系统（CET4,6 registration system）

Python基于Django框架图书管理系统毕业源码案例设计

python基础知识聚合项目，银行系统

Python学生选课系统

Python招聘岗位信息聚合系统（拥有爬虫爬取、数据分析、可视化、互动等功能）

Python程序开发模拟数据库查询系统

python聊天室系统

python量化系统监控

QA_handler-master

tkinter仿写个MIUI系统的计算器

Wagtail是一套基于Python Django的内容管理系统

一个基于Python的Django的疫情管理系统

一个由 Python + Vue + Express 驱动的简单 Valine 评论管理系统。

使用python编写，基于Django和clean-blog前端框架的博客系统

利用python爬取内蒙古师范大学（IMNU）教务系统

华的CMS系统，用Python编写的cms系统

基于Django的python代码填空评测系统

基于java，python爬虫、linux定时任务的易班自动签到系统基础框架

![image](https://ucc.alicdn.com/pic/developer-ecology/jbvj4d7jq5wzg_b25cb7b2834648dca25383322ca710e8.jpeg)

基于python django的多商家网上商城，做了商家后台，有多个商家

基于python-django的web应用教师管理系统

基于python实现的超市管理系统

基于Python爬虫+flask框架+echarts的天气展示系统

基于python的学生宿舍管理系统 - 毕业设计 - 课程设计

基于python的小型超市管理系统

基于python的新版武汉大学教务系统第三方API

基于python的旅游网站， python+django+vue搭建的旅游景区管理系统、旅游景区门票系统 - 毕业设计 - 课程设计

基于python的私有化单点登录(SSO)系统

基于python的药店药品管理系统 - 毕业设计 - 课程设计

外卖点餐系统 Python

如何利用python识别教务处验证码以及爬进教务系统模拟人ji工qi选qiang课ke

学生管理系统（Python + Qt +MySQL）

学生考勤系统 - python

操作系统课设，基于Python flask_socketio 及 WebSocket的多人聊天室

毕设-基于Python的股票自动交易系统的设计与实现

湖南大学(HNU)数据库系统课程大作业 ATM系统前端基于Python的PyQt5，后端基于MySQL

用python做的一个外卖管理系统

用python实现的一款简单的学生管理系统

用python实现的针对电子科技大学网上选课系统的选课脚本，可实现cookie登录，预存课程，多线程选课功能

用Python调用everything进行文件搜索的工具，只适用于Windows系统

用python调用zabbix api，实现自动管理zabbix监控系统

研发了一套基于机器学习方法Scikit-learn(sklearn)与Python结合实现的气象预报以及气象动态展示系统

计算机毕业设计之Spark+Flink+Python考研预测分析 考研院校推荐系统 考研大数据分析大屏

采用Django+Python完成的图书管理系统

重庆大学数据库系统课设Project2：利用Python实现的DBMS

飞虫采集系统，主要采用了python语言，redis+mysql数据库，实现了功能较为强大的实时房价采集分析系统计算机毕业设计之Python+Vue.js协同过滤算法混合新闻推荐系统 新闻网站 新闻发布系统

![image](https://ucc.alicdn.com/images/user-upload-01/104fdfc9dc9f4a59b3a2414127da4e0a.png)

学习知识费力气