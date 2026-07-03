"""
mysql8.0对json有很好的支持，下面我们来学习在mysql中使用json
在navicat中新建一个jsondb数据库，然后上面创建几个表格

"""

import pymysql

# conn = None
# 这里认为你以及成功创建了jsondb数据库
def initdb():
    conn = pymysql.connect(
        host='127.0.0.1', port=3306,
                        user='root', password='root',
                        database='jsondb', charset='utf8mb4'
    )
    return conn

def create_tb_test():
    conn = initdb()
    cursor = conn.cursor()
    sql = """
        CREATE TABLE `tb_test`
        (
        `user_id`    bigint unsigned,
        `login_info` json,
        PRIMARY KEY (`user_id`)
        );
    """
    ret = cursor.execute(sql)
    print(ret)
    conn.commit()
    conn.close() 

def load_tb_test():
    conn = initdb()
    sql = '''
        INSERT INTO `tb_test` 
        VALUES 
            (1, '{"tel": "13122335566", "QQ": "654321", "wechat": "jackfrued"}'),
            (2, '{"tel": "13599876543", "weibo": "wangdachui123"}');
    '''
    cursor = conn.cursor()
    ret = cursor.execute(sql)
    if ret >=1:
        print("inserted data with success....")
    conn.commit()
    conn.close() 

def show_tb_test_data():
    conn = initdb()
    sql = '''
        SELECT `user_id`
            , JSON_UNQUOTE(JSON_EXTRACT(`login_info`, '$.tel')) AS 手机号
            , JSON_UNQUOTE(JSON_EXTRACT(`login_info`, '$.wechat')) AS 微信 
        FROM `tb_test`;
    '''
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()   

def show_tb_test_data2():
    conn = initdb()
    sql = '''
        SELECT `user_id`
            , `login_info` ->> '$.tel' AS 手机号
            , `login_info` ->> '$.wechat' AS 微信
        FROM `tb_test`;
    '''
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()    

## 创建第二个表格
def create_tb_tags():
    conn = initdb()
    cursor = conn.cursor()
    sql = """
        CREATE TABLE `tb_tags`
        (
        `tag_id`   int unsigned NOT NULL COMMENT '标签ID',
        `tag_name` varchar(20)  NOT NULL COMMENT '标签名',
        PRIMARY KEY (`tag_id`)
        );
    """
    ret = cursor.execute(sql)
    print(ret)
    conn.commit()
    conn.close() 

def load_tb_tb_tags():
    conn = initdb()
    sql = '''
        INSERT INTO `tb_tags` (`tag_id`, `tag_name`) 
        VALUES
            (1, '70后'),
            (2, '80后'),
            (3, '90后'),
            (4, '00后'),
            (5, '爱运动'),
            (6, '高学历'),
            (7, '小资'),
            (8, '有房'),
            (9, '有车'),
            (10, '爱看电影'),
            (11, '爱网购'),
            (12, '常点外卖');
    '''
    cursor = conn.cursor()
    ret = cursor.execute(sql)
    if ret >=1:
        print("inserted data with success....")
    conn.commit()
    conn.close() 

def create_tb_users_tags():
    conn = initdb()
    cursor = conn.cursor()
    sql = """
        CREATE TABLE `tb_users_tags`
        (
        `user_id`   bigint unsigned NOT NULL COMMENT '用户ID',
        `user_tags` json            NOT NULL COMMENT '用户标签'
        );
    """
    ret = cursor.execute(sql)
    print(ret)
    conn.commit()
    conn.close() 

def load_tb_user_tags():
    conn = initdb()
    sql = '''
        INSERT INTO `tb_users_tags`
        VALUES
            (1, '[2, 6, 8, 10]'),
            (2, '[3, 10, 12]'),
            (3, '[3, 8, 9, 11]');
    '''
    cursor = conn.cursor()
    ret = cursor.execute(sql)
    if ret >=1:
        print("inserted data with success....")
    conn.commit()
    conn.close() 
# 1.查询爱看电影（有`10`这个标签）的用户ID。
def query_tag1():
    conn = initdb()
    cursor = conn.cursor()
    sql = """
        SELECT `user_id`
        FROM `tb_users_tags`
        WHERE 10 MEMBER OF (`user_tags`->'$');
    """
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close() 
# 2.查询爱看电影（有`10`这个标签）的80后（有`2`这个标签）用户ID。
def query_tag2():
    conn = initdb()
    cursor = conn.cursor()
    sql = """
        SELECT `user_id`
        FROM `tb_users_tags`
        WHERE JSON_CONTAINS(`user_tags`->'$', '[2, 10]');
    """
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close() 

# 3.查询爱看电影或80后或90后的用户ID。
def query_tag3():
    conn = initdb()
    cursor = conn.cursor()
    sql = """
        SELECT `user_id`
        FROM `tb_users_tags`
        WHERE JSON_OVERLAPS(user_tags->'$', '[2, 3, 10]');
    """
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close() 

if __name__ == '__main__':
    # create_tb_test() 
    # load_tb_test()
    # show_tb_test_data()   
    # show_tb_test_data2()   
    # create_tb_tags()
    # load_tb_tb_tags()
    # create_tb_users_tags()
    # load_tb_user_tags()
    # query_tag1()
    # query_tag2()
    query_tag3()