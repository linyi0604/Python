#coding:utf8

from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField,SubmitField
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

# 设置数据库链接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/flask'
app.config['SQLALCHEMY_COMMIT_ON_TEAMDOWN'] = True
# 设置自动跟踪修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY']='s'

# 设置实例化数据库对象
db = SQLAlchemy(app)

# 定义 数据库表 作者
class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),unique=True)
    email = db.Column(db.String(64))
    # 关系字段
    au_book = db.relationship('Book',backref='author')

    def __repr__(self):
        return str(self.name)

# 定义数据库标 书
class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer,primary_key=True)
    info = db.Column(db.String(32),unique=True)
    lead = db.Column(db.String(32))
    au_book = db.Column(db.Integer,db.ForeignKey('author.id'))
    def __repr__(self):
        return str(self.info)

# 一个表单
class Append(FlaskForm):
    au_info = StringField(validators=[DataRequired()])
    bk_info = StringField(validators=[DataRequired()])
    submit = SubmitField(u'添加')

@app.route('/',methods=['POST','GET'])
def index():
    # 查询所有作者和图书信息
    authors = Author.query.all()
    books = Book.query.all()
    form = Append()
    if request.method == "GET":
        return render_template('index.html', authors=authors, books=books, form=form)

    else:   # 发送的是post请求
        # 如果提交表单经过验证
        if form.validate_on_submit():
            au = form.au_info.data
            bk = form.bk_info.data
            print au, bk
            # 插入数据库
            db_au = Author(name=au)
            db_bk = Book(info=bk)
            # 添加
            db.session.add_all([db_au,db_bk])
            db.session.commit()

            authors = Author.query.all()
            books = Book.query.all()

        return render_template('index.html',authors=authors,books = books,form = form)

@app.route('/del_book/<id>')
def delete_book(id):

    book = Book.query.filter_by(id=id).first()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/del_author/<id>')
def delete_author(id):
    author = Author.query.filter_by(id=id).first()
    db.session.delete(author)
    db.session.commit()
    return redirect(url_for("index"))




if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    # 生成数据
    au_xi = Author(name='我吃西红柿', email='xihongshi@163.com')
    au_qian = Author(name='萧潜', email='xiaoqian@126.com')
    au_san = Author(name='唐家三少', email='sanshao@163.com')
    bk_xi = Book(info='吞噬星空', lead='罗峰')
    bk_xi2 = Book(info='寸芒', lead='李杨')
    bk_qian = Book(info='飘渺之旅', lead='李强')
    bk_san = Book(info='冰火魔厨', lead='融念冰')
    # 把数据提交给用户会话
    db.session.add_all([au_xi, au_qian, au_san, bk_xi, bk_xi2, bk_qian, bk_san])
    # 提交会话
    db.session.commit()
    app.run(debug=True)