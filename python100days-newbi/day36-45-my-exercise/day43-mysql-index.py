"""
mysql默认是不使用索引的，我们可以使用explain select xx from xx 来查看，如果key是null,说明没有使用索引
我们可以使用create index 命令来创建索引
"""
import pymysql

def initdb():
    conn = pymysql.connect(
        host='127.0.0.1', port=3306,
                        user='root', password='root',
                        database='school', charset='utf8mb4'
    )
    return conn

def create_index(tb,col):
    conn = initdb()
    # create index idx_stu_name on tb_student(stu_name)
    sql = f"""
     create index idx_{col} on {tb}({col})
    """
    cursor = conn.cursor()
    res = cursor.execute(sql)
    print(res)
    conn.commit()
    conn.close()

def explain_select():
    conn = initdb()
    sql = """
      explain select * from tb_student where stu_name='林震南'
    """    
    cursor = conn.cursor()
    res = cursor.execute(sql)
    print(cursor.fetchall())
    conn.close()

def del_index(tb,col):
    conn = initdb()
    # sql = f"""
    #   alter table {tb} drop index idx_{col};
    # """    
    sql = f"""
      drop index idx_{col} on {tb};
    """    
    cursor = conn.cursor()
    res = cursor.execute(sql)
    print(res)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    #  create_index('tb_student',"stu_name")
#    create_index('tb_student',"stu_birth") # idx_tb_birth
     explain_select()
    #  del_index('tb_student','stu_birth')
    #  del_index('tb_student','stu_name')