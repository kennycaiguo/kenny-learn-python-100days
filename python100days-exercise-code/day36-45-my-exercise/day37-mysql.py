"""
pip install pymysql cryptography
前提，已经安装mysql并且设置为服务
"""
import pymysql 

def insert_data():
    no = int(input('部门编号: '))
    name = input('部门名称: ')
    location = input('部门所在地: ')

    # 1.创建连接对象，也就是连接到数据库
    conn = pymysql.connect(host='127.0.0.1', port=3306,
                        user='root', password='root',
                        database='company', charset='utf8mb4')
    # print(conn) # <pymysql.connections.Connection object at 0x000001F28FF5BF50>
    try:
    # 2.获取游标
        with conn.cursor() as cursor:
            # 插入数据
            row = cursor.execute("insert into dept values(%s,%s,%s);",(no,name,location))
            if row > 0 :
                print("new data added...")
            # 提交事务    
            conn.commit()
    except pymysql.MySQLError as e:
        print(e,type(e))
    finally:
        conn.close()        


def show_all():
     # 1.创建连接对象，也就是连接到数据库
    conn = pymysql.connect(host='127.0.0.1', port=3306,
                        user='root', password='root',
                        database='company', charset='utf8mb4')
    
    try:
    # 2.获取游标
        with conn.cursor() as cursor:
            # 插入数据
            cursor.execute("select * from dept;")
            # print(rows) # number of rows
            # print(cursor.fetchall())
            rows = cursor.fetchall()
            for row in rows:
                for col in row:
                    print(col,end=" ")
                print()    
    except pymysql.MySQLError as e:
        print(e,type(e))
    finally:
        conn.close()   

def query_data(sql,param):
      # 1.创建连接对象，也就是连接到数据库
    conn = pymysql.connect(host='127.0.0.1', port=3306,
                        user='root', password='root',
                        database='company', charset='utf8mb4')
    
    try:
    # 2.获取游标
        with conn.cursor() as cursor:
            # 插入数据
            cursor.execute(sql,param)
            # print(rows) # number of rows
            # print(cursor.fetchall())
            rows = cursor.fetchall()
            for row in rows:
                for col in row:
                    print(col,end=" ")
                print()    
    except pymysql.MySQLError as e:
        print(e,type(e))
    finally:
        conn.close()   

def update_data(update_sql,param):
    # 1.创建连接对象，也就是连接到数据库
    conn = pymysql.connect(host='127.0.0.1', port=3306,
                        user='root', password='root',
                        database='company', charset='utf8mb4')
    # print(conn) # <pymysql.connections.Connection object at 0x000001F28FF5BF50>
    try:
    # 2.获取游标
        with conn.cursor() as cursor:
            # do update process
            rows = cursor.execute(update_sql,param)
            if rows > 0 :
                 print("update successful...")
            # 提交事务    
            conn.commit()
           
    except pymysql.MySQLError as e:
        print(e,type(e))
    finally:
        conn.close()   

def del_one(delsql,param):
    # 1.创建连接对象，也就是连接到数据库
    conn = pymysql.connect(host='127.0.0.1', port=3306,
                        user='root', password='root',
                        database='company', charset='utf8mb4')
    # print(conn) # <pymysql.connections.Connection object at 0x000001F28FF5BF50>
    try:
    # 2.获取游标
        with conn.cursor() as cursor:
            # do update process
            rows = cursor.execute(delsql,param)
            if rows > 0 :
                 print("delete successful...")
            # 提交事务    
            conn.commit()
           
    except pymysql.MySQLError as e:
        print(e,type(e))
    finally:
        conn.close()   


if __name__ == '__main__':
   # insert_data()
#    show_all()
#    query_data("select * from dept where no=%s",(3,))
#    update_data("update dept set name=%s where no=%s;",("tech department",3))
     del_one("delete from dept where no=%s",(3,))