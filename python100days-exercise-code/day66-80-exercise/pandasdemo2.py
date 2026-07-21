"""
DataFrame

"""
import pandas as pd
import numpy as np

# method 1
# scores = np.random.randint(60,101,(5,3))
# print(scores)
# subjects = ['Chinese',"Math",'English']
# stu_ids = np.arange(1000,1005)
# df = pd.DataFrame(data=scores,columns=subjects,index=stu_ids)
# print(df)

# method 2
scores = {
     'Chinese':[55,60,90,80,70],
     'Math':[90,80,75,65,95],
     'English':[60,65,58,75,68]
}
stu_ids = np.arange(1000,1005)
df2 = pd.DataFrame(data=scores,index=stu_ids)
# print(df2)


df3 = pd.read_csv("./data.csv")
# print(df3)

df4 = pd.read_excel('./emp.xlsx',index_col='empid')
# print(df4)

## create dataframe obj from a datatable
# 需要注意的是这个数据库里面的数据表必须存在
def pandas_pymysql1():
    import pymysql

    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='root',
        database='school'
    )

    # print(conn) # <pymysql.connections.Connection object at 0x000001F871579710>
    # 通过SQL从数据库二维表读取数据创建DataFrame
    # stus_df = pd.read_sql("select * from tb_student",conn,index_col='stu_id')
    stus_df = pd.read_sql_query("select * from tb_student",conn,index_col='stu_id')
    print(stus_df) 

def pandas_sqlalchemy():
    import pymysql
    from sqlalchemy import create_engine

    ## 连接字符串格式 用户名：密码@主机ip:端口/数据库名称?charset=utf8mb4
    engine =create_engine("mysql+pymysql://root:root@127.0.0.1:3306/school?charset=utf8mb4")
    stu_df = pd.read_sql("select * from tb_student",engine,index_col='stu_id')
    print(stu_df)
    engine.connect().close() # 使用完毕后关闭数据库

# pandas_sqlalchemy() # ok

## 还可以直接读取数据表,调用pd.read_sql_table(...)方法
def pandas_sqlalchemy2():
    import pymysql
    from sqlalchemy import create_engine

    ## 连接字符串格式 用户名：密码@主机ip:端口/数据库名称?charset=utf8mb4
    engine =create_engine("mysql+pymysql://root:root@127.0.0.1:3306/school?charset=utf8mb4")
    stu_df = pd.read_sql_table("tb_student",engine,index_col='stu_id')
    # print(stu_df)
    # print(stu_df.info())
    # print(stu_df['stu_name'])
    # print(stu_df.iloc[3]) # 获取的是数据表的第4行数据，或者说第四条记录
    # print(stu_df.iloc[3]['stu_name']) # 王语嫣
    # print(stu_df.loc[222])  # loc[索引值]否则报错
    # print(stu_df[1:4]) # 切片索引，获取第2行到第四行的数据
    # print(stu_df.stu_birth) # 获取dataframe的一列
    # print(stu_df['stu_name']) # 获取dataframe的一列,方法2
    # print(stu_df[stu_df.stu_sex==0]) # 选取所有女生
    print(stu_df.query('stu_sex!=0')) # query查询方法

    engine.connect().close() # 使用完毕后关闭数据库

pandas_sqlalchemy2()    
