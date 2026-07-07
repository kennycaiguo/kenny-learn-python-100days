from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return 'Welcome to Home page'

@app.route('/index')
def index():  # put application's code here
    users = [
        {"id":1001,"name":"Jackline","gender":"Female","email":"jl123@gmail.com"},
        {"id":1002,"name":"Bennet","gender":"Male","email":"ben123@gmail.com"},
        {"id":1003,"name":"Tracy","gender":"Female","email":"tr1234@gmail.com"}
    ]
    return render_template("index.html",title="用户列表",users=users)


if __name__ == '__main__':
    app.run()
