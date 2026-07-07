from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# 新增用户功能
@app.route('/add/user', methods=['GET', 'POST'])
def add_user():  # put application's code here
    if request.method == "GET":  # 如果是get请求
        return render_template("add_user.html")
    # 如果是post请求
    user = request.form.get("user")
    pwd = request.form.get("pwd")
    mobile = request.form.get("mobile")
    print(f"user:{user},password:{pwd},Phone:{mobile}")
    # 保存数据到MySQL数据库中
    # 1.连接MySQL
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root", charset='utf8', db="unicom")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 2.保存数据
    sql = "insert into admin(username,password,mobile) values(%s,%s,%s)"
    cursor.execute(sql, [user, pwd, mobile])
    conn.commit()  # 一定要提交
    print("插入数据成功")
    # 3.关闭连接
    cursor.close()
    conn.close()
    return "提交数据成功"


# 查询所有用户功能
@app.route("/users")
def getUsers():
    # 1.连接MySQL
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root", charset='utf8', db="unicom")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 2.查询所有数据
    sql = "select * from admin;"
    cursor.execute(sql)
    users = cursor.fetchall()
    # 3.关闭连接
    cursor.close()
    conn.close()
    return render_template("users.html",users=users)


if __name__ == '__main__':
    app.run()
