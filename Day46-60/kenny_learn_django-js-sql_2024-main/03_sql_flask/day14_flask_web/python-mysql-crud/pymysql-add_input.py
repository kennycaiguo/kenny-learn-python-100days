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

# 1.2让用户输入我们的数据:
name = input("请输入用户名:")
pwd = input("请输入密码:")
ph = input("请输入手机号码")
# 2.发送指令
# 1>比如新增一条数据
# sqlcmd = "insert into admin (username,password,mobile) values('Jackma','123','13532619997')"
# 1.2>使用预编译sql,先用占位符占位
sqlcmd = "insert into admin (username,password,mobile) values(%s,%s,%s)"
# 1.3> 然后定义一个数据元组
data = [name,pwd,ph]
# 1.4 把数据传递进execte方法里面
cursor.execute(sqlcmd,data)
# 2>需要提交请求,否则无法成功
conn.commit()
# 3.关闭连接
cursor.close()
conn.close()
