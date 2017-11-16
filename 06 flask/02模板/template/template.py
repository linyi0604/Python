#coding:utf8
from flask import Flask,render_template,redirect,url_for,request,session,flash
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,PasswordField
from wtforms.validators import DataRequired,EqualTo

app = Flask(__name__)

'''
1 向模板传送 参数
'''
@app.route('/')
def index():
    name = 'Python'
    context = {
        'name':'Python',
        'age' : 18 ,
        'num_list': [1,2,3,4,5,6,7,8,9,10]
    }
    return render_template('index.html',context=context,name=name )

'''
2 反向路由
url_for(视图函数名)) 能够返回视图的相对url
利用redirect( url_for(视图函数) ) 实现重定向
'''
@app.route('/redirect')
def redi():
    redir = url_for('index',_external=True)
    print(redir)
    return redirect(redir)


'''
3 过滤器:

    safe 禁用转义  <p>{{ '<em>hello</em>' | safe }}</p>
    capitalize 首字母大写  <p>{{ 'hello' | capitalize }}</p>
    lower 小写  <p>{{ 'HELLO' | lower }}</p>
    upper 大写  <p>{{ 'hello' | upper }}</p>
    title 每个单词首字母大写  <p>{{ 'hello' | title }}</p>
    trim 去掉首位空格   <p>{{ ' hello world ' | trim }}</p>
    reverse 反转字符串   <p>{{ 'olleh' | reverse }}</p>
    format 格式化  <p>{{ '%s is %d' | format('name',17) }}</p>
    striptags 删掉html标签    <p>{{ '<em>hello</em>' | striptags }}</p>

列表操作:
    first 取第一个元素 <p>{{ [1,2,3,4,5,6] | first }}</p>
    last 取最后一个元素   <p>{{ [1,2,3,4,5,6] | last }}</p>
    length 获取列表长度    <p>{{ [1,2,3,4,5,6] | length }}</p>
    sum 列表求和    <p>{{ [1,2,3,4,5,6] | sum }}</p>
    sort 列表排序   <p>{{ [6,2,3,1,5,4] | sort }}</p>

语句块过滤:
  {% filter upper %}
    this is a Flask Jinja2 introduction
  {% endfilter %}
  
自定义过滤器: 两种方式
    1 app.add_template_filter(函数名,过滤器名)
    2 @app.template_filter(过滤器名)
'''
@app.route('/filter')
def filter():
    str = 'abCdeF hello woRld'
    li = [1,2,5,4,3,76,65,8,9]
    return render_template('filter.html',str=str,li=li)
# 自定义过滤器
def hahah(li):
    return str(li)+'hahaha'
app.add_template_filter(hahah,'hahah')

@app.template_filter('heihei')
def heihei(li):
    return str(li) + 'heihei'

'''
3 web表单 WTForms
'''
# 获取常规表单数据的方法
@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username , password)
    return render_template('form.html')


# 利用Flask的 WTF 实现表单
# 配置 csrf_token 的生成项
app.config['SECRET_KEY'] = 'python12'
# 配置表单类
class Form(FlaskForm):
    # user字段 text类型input框 校验输入数据
    user = StringField(validators=[DataRequired()])
    # equalto 检测 与ps2 内容是否一样
    ps = PasswordField(validators=[DataRequired(),EqualTo('ps2','err')])
    ps2=PasswordField(validators=[DataRequired()])
    submit = SubmitField()

# 利用Flask的 WTF 实现表单
@app.route('/WTForm',methods=['GET','POST'])
def wtForm():
    form = Form()  # 拿到一个表单对象
    if form.validate_on_submit(): # 能够自动检验 提交的表单是否经过验证 返回True或者False
        # 获取表单数据
        user = form.user.data
        ps = form.ps.data
        ps2 = form.ps2.data
        print user,ps,ps2
    if request.method == "POST":
        # flask 操作后端
        flash(u'信息发生错误!')

    print(form.validate_on_submit()) #能够检验 提交是否经过验证,返回True或者False


    return render_template('form.html',form=form)


'''
4 宏 继承 包含 模板的使用
'''
@app.route('/macro')
def macro():
    return render_template('macro.html')


if __name__ == '__main__':
    app.run(debug=True)
