"""
利用pymysql来查询数据
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

def query_by_id():
    id = input("请输入你需要查询的用户的id:")
    sql = "select * from admin where id=%s"
    cursor.execute(sql,[id])
    results = cursor.fetchall() # 先执行sql查询语句,然后在用cursor.fetchall()获取数据(当然,如果你确定只有一条数据,可以使用fetchaone)
    for res in results:
        print(res)

if __name__ == '__main__':
    query_by_id()