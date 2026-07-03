import pymysql

conn = None

def doAddJob(conn,addsql,tb_name):
    if conn == None:
        conn = pymysql.connect(host='127.0.0.1', port=3306,
                        user='root', password='root',
                        database='school', charset='utf8mb4')
    cursor = conn.cursor()
    rows = cursor.execute(addsql)  
    if rows>=1:
        print(f"table {tb_name} is loaded ")
    conn.commit()  
    conn.close  
"""
插入数据学生表格
"""
def load_stu():
 
    # print(conn)
    tb = 'tb_student'

    sql = f"""
          -- 插入学生数据
        INSERT INTO {tb}
            (`stu_id`, `stu_name`, `stu_sex`, `stu_birth`, `stu_addr`, `col_id`) 
        VALUES
            (1001, '杨过', 1, '1990-3-4', '湖南长沙', 1),
            (1002, '任我行', 1, '1992-2-2', '湖南长沙', 1),
            (1033, '王语嫣', 0, '1989-12-3', '四川成都', 1),
            (1572, '岳不群', 1, '1993-7-19', '陕西咸阳', 1),
            (1378, '纪嫣然', 0, '1995-8-12', '四川绵阳', 1),
            (1954, '林平之', 1, '1994-9-20', '福建莆田', 1),
            (2035, '东方不败', 1, '1988-6-30', NULL, 2),
            (3011, '林震南', 1, '1985-12-12', '福建莆田', 3),
            (3755, '项少龙', 1, '1993-1-25', '四川成都', 3),
            (3923, '杨不悔', 0, '1985-4-17', '四川成都', 3);
    """
    doAddJob(conn,sql,tb)
      

# 加载老师表格
def load_teacher():
    tb = 'tb_teacher'
    sql = f"""
        INSERT INTO {tb}
    (`tea_id`, `tea_name`, `tea_title`, `col_id`) 
    VALUES 
        (1122, '张三丰', '教授', 1),
        (1133, '宋远桥', '副教授', 1),
        (1144, '杨逍', '副教授', 1),
        (2255, '范遥', '副教授', 2),
        (3366, '韦一笑', DEFAULT, 3);
    """
    doAddJob(conn,sql,tb)


def load_course():
    tb = 'tb_course'
    sql = f"""
        INSERT INTO {tb} 
        (`cou_id`, `cou_name`, `cou_credit`, `tea_id`) 
        VALUES 
            (1111, 'Python程序设计', 3, 1122),
            (2222, 'Web前端开发', 2, 1122),
            (3333, '操作系统', 4, 1122),
            (4444, '计算机网络', 2, 1133),
            (5555, '编译原理', 4, 1144),
            (6666, '算法和数据结构', 3, 1144),
            (7777, '经贸法语', 3, 2255),
            (8888, '成本会计', 2, 3366),
            (9999, '审计学', 3, 3366);
    """
    doAddJob(conn,sql,tb)

def load_record():
    tb = 'tb_record'
    sql = f"""
        -- 插入选课数据
        INSERT INTO {tb} 
            (`stu_id`, `cou_id`, `sel_date`, `score`) 
        VALUES 
            (1001, 1111, '2017-09-01', 95),
            (1001, 2222, '2017-09-01', 87.5),
            (1001, 3333, '2017-09-01', 100),
            (1001, 4444, '2018-09-03', NULL),
            (1001, 6666, '2017-09-02', 100),
            (1002, 1111, '2017-09-03', 65),
            (1002, 5555, '2017-09-01', 42),
            (1033, 1111, '2017-09-03', 92.5),
            (1033, 4444, '2017-09-01', 78),
            (1033, 5555, '2017-09-01', 82.5),
            (1572, 1111, '2017-09-02', 78),
            (1378, 1111, '2017-09-05', 82),
            (1378, 7777, '2017-09-02', 65.5),
            (2035, 7777, '2018-09-03', 88),
            (2035, 9999, '2019-09-02', NULL),
            (3755, 1111, '2019-09-02', NULL),
            (3755, 8888, '2019-09-02', NULL),
            (3755, 9999, '2017-09-01', 92);
    """
    doAddJob(conn,sql,tb)

def load_college():
    tb = 'tb_college'
    sql = f"""
        -- 插入学院数据
        INSERT INTO {tb} 
            (`col_name`, `col_intro`) 
        VALUES 
            ('计算机学院', '计算机学院1958年设立计算机专业，1981年建立计算机科学系，1998年设立计算机学院，2005年5月，为了进一步整合教学和科研资源，学校决定，计算机学院和软件学院行政班子合并统一运作、实行教学和学生管理独立运行的模式。 学院下设三个系：计算机科学与技术系、物联网工程系、计算金融系；两个研究所：图象图形研究所、网络空间安全研究院（2015年成立）；三个教学实验中心：计算机基础教学实验中心、IBM技术中心和计算机专业实验中心。'),
            ('外国语学院', '外国语学院设有7个教学单位，6个文理兼收的本科专业；拥有1个一级学科博士授予点，3个二级学科博士授予点，5个一级学科硕士学位授权点，5个二级学科硕士学位授权点，5个硕士专业授权领域，同时还有2个硕士专业学位（MTI）专业；有教职员工210余人，其中教授、副教授80余人，教师中获得中国国内外名校博士学位和正在职攻读博士学位的教师比例占专任教师的60%以上。'),
            ('经济管理学院', '经济学院前身是创办于1905年的经济科；已故经济学家彭迪先、张与九、蒋学模、胡寄窗、陶大镛、胡代光，以及当代学者刘诗白等曾先后在此任教或学习。');
    """
    doAddJob(conn,sql,tb)

def query_data(querysql,params=None):
    global conn
    if conn == None:
        conn = pymysql.connect(host='127.0.0.1', port=3306,
                        user='root', password='root',
                        database='school', charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute(querysql,params)  
    rows = cursor.fetchall()
    for row in rows:
        print(row)  
    conn.close   

def add_col(sql):
    global conn
    if conn == None:
        conn = pymysql.connect(host='127.0.0.1', port=3306,
                        user='root', password='root',
                        database='school', charset='utf8mb4')  
    cursor = conn.cursor()
    row = cursor.execute(sql) 
    if row > 0:
        print("success...")     
    conn.commit()    
    conn.close() 

def doUpdateJob(conn,sql,tb,params=None):
    if conn == None:
        conn = pymysql.connect(host='127.0.0.1', port=3306,
                        user='root', password='root',
                        database='school', charset='utf8mb4')
    cursor = conn.cursor()
    rows = cursor.execute(sql,params)  
    if rows>=1:
        print(f"table {tb} updated ")
    conn.commit()  
    conn.close  


def test_doupdate():
    conn = pymysql.connect(host='127.0.0.1', port=3306,
                        user='root', password='root',
                        database='school', charset='utf8mb4')
    #  cur = conn.cursor()
    #  cur.execute("update tb_student set age=%s where stu_id=%s;",(23,1002))
    #  conn.commit()
    #  conn.close()
    doUpdateJob(conn,"update tb_student set age=%s where stu_id=%s;",'tb_student',(25,1033))

def update_stu():
    sql = "update tb_student set age=%s where stu_id=%s;"
    params = (22,3923)
    doUpdateJob(conn,sql,'tb_student',(params[0],params[1])) # 两个占位符的传递值方法

def del_record(conn,delsql,tb,params=None):
    if conn == None:
        conn = pymysql.connect(host='127.0.0.1', port=3306,
                        user='root', password='root',
                        database='school', charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;") #关闭外键检查，可能有些表不能这么做
    row = cursor.execute(delsql,params)
    if row > 0:
        print(f"Deleted Record From {tb}")
    conn.commit()  
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;") #打开外键检查
    conn.close  

# dcl 数据操作权限语句
def add_user(conn,params): #新增用户
    if conn == None:
        conn = pymysql.connect(host='127.0.0.1', port=3306,
                        user='root', password='root',
                        database='school', charset='utf8mb4')
    cursor = conn.cursor()
    res = cursor.execute("CREATE USER %s@%s IDENTIFIED BY %s;",(params[0],params[1],params[2]))
    print(res)
    conn.commit()  
    conn.close 

def del_user(conn,params): #删除用户
    if conn == None:
        conn = pymysql.connect(host='127.0.0.1', port=3306,
                        user='root', password='root',
                        database='school', charset='utf8mb4')
    cursor = conn.cursor()
    res = cursor.execute("DROP USER IF EXISTS %s@%s;",(params[0],params[1]))
    print(res)
    conn.commit()  
    conn.close 

# 授予权限
def grant_privileges(conn,params): 
    if conn == None:
        conn = pymysql.connect(host='127.0.0.1', port=3306,
                        user='root', password='root',
                        database='school', charset='utf8mb4')
    cursor = conn.cursor()
    # res = cursor.execute("GRANT SELECT ON school.tb_college TO %s@%s;",(params[0],params[1]))
    res = cursor.execute("GRANT SELECT ON school.tb_college TO %s@%s;",params)
    print(res)
    conn.commit()  
    conn.close 

#查看数据库的所有用户
def get_all_user(conn):
    if conn == None:
        conn = pymysql.connect(host='127.0.0.1', port=3306,
                        user='root', password='root',
                        database='mysql', charset='utf8mb4') # 查看用户的时候，数据库名称必须是mysql
    cursor = conn.cursor()
    res = cursor.execute("SELECT User, Host FROM user;")
    print(res)  # 当前有4个用户
    for row in cursor.fetchall():
        print(row)
    conn.close 
# 我们也可以让 wangdachui 对指定 数据库的所有对象都具有查询权限，代码如下所示。
def grant_privileges2(conn,params):
    if conn == None:
        conn = pymysql.connect(host='127.0.0.1', port=3306,
                        user='root', password='root',
                        database='school', charset='utf8mb4')
    cursor = conn.cursor()
    # res = cursor.execute("GRANT SELECT ON %s.* TO %s@%s;",params)
    sql = f"GRANT SELECT ON {params[0]}.* TO '{params[1]}'@'{params[2]}';"
    # print(sql)
    res = cursor.execute(sql)
    print(res)
    # 刷新权限使其生效
    cursor.execute("FLUSH PRIVILEGES;")
    conn.commit()  
    conn.close 

if __name__ == '__main__':
    # load_stu()    
    # load_teacher()
    # load_course()
    # load_record()
    # load_college()
    # query_data("select * from tb_student")
    # query_data("select * from tb_student where col_id=%s",(3,))
    # query_data("select * from tb_student where col_id<>%s",(3,))
    # query_data("select * from tb_course where cou_name like '%计算机%'")
    # add_col("alter table tb_student add column `age` int not null comment '年龄'")
    # doUpdateJob(conn,"update tb_student set age=%s where stu_id=%s",(3923,20))
    # test_doupdate()
    # update_stu()
    # del_record(conn,"delete from tb_student where stu_id=%s;",'tb_student',(2035,))
    # del_user(conn,('wangdachui','%'))
    # del_user(conn,('wangdachui','192.168.0.%'))
    # get_all_user(conn)
    #  add_user(conn,('wangdachui','%','Wang.618'))
    # grant_privileges(conn,('wangdachui','%'))
    grant_privileges2(conn,('school','wangdachui','%'))