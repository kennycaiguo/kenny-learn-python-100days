"""
利用pymysql来删除数据
"""
import pymysql
# pymysql操作数据库,使用用户输入的数据和预编译sql
# 1.连接MySQL数据库
host = "127.0.0.1"
port = 3306
user = "root"
pwd = "root"
charset = "utf8"
db = "unicom"

# 创建数据库连接对象
conn = pymysql.connect(host=host,port=port,user=user,passwd=pwd,charset=charset,db=db)
# 创建游标对象用来存取数据
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

id = input("请输入需要删除的用户的id: ")
sql = "delete from admin where id=%s"
cursor.execute(sql,[id,])
conn.commit()
print("删除数据成功")
