#coding:utf8

from flask import Flask
from login_demo import login    # 从分路由倒入路由函数
from register_demo import register
app = Flask(__name__)


# 注册蓝图 第一个参数 是蓝图对象
app.register_blueprint(login)
app.register_blueprint(register)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    print( app.url_map )
    app.run()
