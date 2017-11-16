#coding:utf8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 设置链接数据库的url
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:mysql@127.0.0.1:3306/flask'

# 每次请求结束后自动提交数据
app.config['SQLALCHEMY_COMMIT_ON_TEAMDOWN'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 查询时会显示原始的sql语句
app.config['SQLALCHEMY_ECHO'] = True

# 注册数据库
db = SQLAlchemy(app)




class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义列对象
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)

    # 关系字段 用于两个方向查
    user = db.relationship('User',backref='rel')

    # repr() 方法现实一个可读字符串
    def __repr__(self):
        return str(self.name)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True,index=True)
    email = db.Column(db.String(64),unique=True)
    pswd = db.Column(db.String(64))
    role_id = db.Column(db.Integer,db.ForeignKey("roles.id"))

    def __repr__(self):
        return str(self.name)


if __name__ == '__main__':
    db.drop_all()   # 删除表
    db.create_all() # 创建表
    ro1 = Role(name = 'admin')  # 创建对象
    ro2 = Role(name = 'user' )
    # 向数据库添加数据
    db.session.add_all([ro1,ro2])
    # 提交
    # db.session.commit()


    us1 = User(name='wang', email='wang@163.com', pswd='123456', role_id=ro1.id)
    us2 = User(name='zhang', email='zhang@189.com', pswd='201512', role_id=ro2.id)
    us3 = User(name='chen', email='chen@126.com', pswd='987654', role_id=ro2.id)
    us4 = User(name='zhou', email='zhou@163.com', pswd='456789', role_id=ro1.id)
    db.session.add_all([us1, us2, us3, us4])
    db.session.commit()


    app.run(debug=True)

