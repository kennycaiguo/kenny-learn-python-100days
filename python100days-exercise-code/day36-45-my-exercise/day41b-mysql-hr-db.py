"""
窗口函数
  <窗口函数> OVER (PARTITION BY <用于分组的列名> ORDER BY <用于排序的列名>  ROWS BETWEEN ... AND ...)
  <窗口函数> OVER (PARTITION BY <用于分组的列名> ORDER BY <用于排序的列名> RANGE BETWEEN ... AND ...)
  上面语法中，窗口函数的位置可以放以下两种函数：

    1. 专用窗口函数，包括：`lead`、`lag`、`first_value`、`last_value`、`rank`、`dense_rank`和`row_number`等。
    2. 聚合函数，包括：`sum`、`avg`、`max`、`min`和`count`等。

    下面为大家举几个使用窗口函数的简单例子，我们直接使用上一课创建的 hrs 数据库。
"""
import pymysql

def initdb():
    conn = pymysql.connect(
        host='127.0.0.1', port=3306,
                        user='root', password='root',
                        database='hrs', charset='utf8mb4'
    )
    return conn
# 例子1：查询按月薪从高到低排在第4到第6名的员工的姓名和月薪。
def query_data1():
    conn = initdb()
    sql = """
     SELECT * 
        FROM (SELECT `ename`
                    , `sal`
                    , ROW_NUMBER() over (ORDER BY `sal` DESC) AS `rk`
                FROM `tb_emp`) AS `temp`
        WHERE `rk` between 4 and 6;
    """
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
    conn.close() # 用完了，需要关闭连接

# 例子2：查询每个部门月薪最高的两名的员工的姓名和部门名称。
def query_data2():
    conn = initdb()
    sql = """
     select `ename`, `sal`, `dname` 
        from (
            select 
                `ename`, `sal`, `dno`,
                rank() over (partition by `dno` order by `sal` desc) as `rank`
            from `tb_emp`
        ) as `temp` natural join `tb_dept` where `rank`<=2;
    """
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
    conn.close() # 用完了，需要关闭连接



if __name__ == '__main__':
    # query_data1()    
    query_data2()    