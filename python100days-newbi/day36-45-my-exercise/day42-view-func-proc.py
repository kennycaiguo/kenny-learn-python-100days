"""
为了讲解视图、函数和过程，我们需要先创建名为 hrs 的数据库并为其二维表添加数据。code文件夹里面有对应的sql文件。
用navicat导入并且执行对应的sql语句即可
创建函数和视图比较复杂调用比较简单
# 调用视图： select * from `vw_emp_simple`; 
 # 调用函数： select fn_truncate_string('和我在成都的街头走一走，直到所有的灯都熄灭了也不停留', 10) as short_string;
注意:navicat的过程和函数都保存在函数并且里面的,fx是函数,px是指过程
调用过程：call sp_upgrade_salary();
"""
import pymysql

def initdb():
    conn = pymysql.connect(
        host='127.0.0.1', port=3306,
                        user='root', password='root',
                        database='hrs', charset='utf8mb4'
    )
    return conn
# 创建视图
def create_view():
    conn = initdb()
    sql = """
     create view `vw_emp_simple`
        as
        select  `eno`,
                `ename`,
                `job`,
                `dno`
        from  `tb_emp`;
    """
    cursor = conn.cursor()
    ret = cursor.execute(sql)
    print(ret)
    conn.commit()
    conn.close() # 用完了，需要关闭连接
#函数
def create_func():
    conn = initdb()
    sql = """
        create function fn_truncate_string2(
            content varchar(10000),
            max_length int unsigned
        ) returns varchar(10000) no sql
        begin
            declare result varchar(10000) default content;
            if char_length(content) > max_length then
                set result = left(content, max_length);
                set result = concat(result, '……');
            end if;
            return result;
        end 
    """
    cursor = conn.cursor()
    ret = cursor.execute(sql)
    print(ret)
    conn.commit()
    conn.close() # 用完了，需要关闭连接

def query_view():
    conn = initdb()
    sql = """
     select * from `vw_emp_simple`
    """
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
    conn.close() # 用完了，需要关闭连接

def call_func():
    conn = initdb()
    sql = """
     select fn_truncate_string('和我在成都的街头走一走，直到所有的灯都熄灭了也不停留', 10) as short_string;
    """
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
    conn.close() # 用完了，需要关闭连接   

# 创建过程,这个过程没有返回值
def create_proc():
    conn = initdb()
    sql = """
        create procedure sp_upgrade_salary()
        begin
            declare flag boolean default 1;
            -- 定义一个异常处理器
            declare continue handler for sqlexception set flag=0;

            -- 开启事务环境
            start transaction;
            
            update tb_emp set sal=sal+300 where dno=10;
            update tb_emp set sal=sal+800 where dno=20;
            update tb_emp set sal=sal+500 where dno=30;

            -- 提交或回滚事务
            if flag then
                commit;
            else
                rollback;
            end if;
        end 
    """
    cursor = conn.cursor()
    ret = cursor.execute(sql)
    print(ret)
    conn.commit()
    conn.close() # 用完了，需要关闭连接

def call_proc():
    conn = initdb()
    sql = """
     call sp_upgrade_salary();
    """
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
    conn.close() # 用完了，需要关闭连接   
    

if __name__ == '__main__':
    # create_view()
    # create_func()
    # query_view()
    # call_func()
    # create_proc()
    call_proc()
    

