#coding:utf8
# 导入flask
from flask import Flask,abort,redirect,make_response,request
from werkzeug.routing import BaseConverter


# Flask 接受一个参数__name__ 作用是指明应用的位置
app = Flask(__name__)



'''
1 建立一个前后台链接
装饰器的作用是陆游映射到视图函数index
访问根目录就会进入index视图函数
'''
@app.route('/')
def index():
    # 返回后会调用make_response
    return "你好 世界!"


'''
2 给路由传参数
传递的参数在<name>当中 这个变量名称也要传递给视图函数
可以在<int:name> 或者<string:name> 指定传递参数的类型
不指定类型默认使用string类型
'''
@app.route('/attr/<string:attr>')
def attr(attr):
    return "hello,%s"%attr


'''
3 返回网络状态码的两种方式
    01 return 字符串,状态码
    02 abort(状态码)
200 成功
300 重定向
404 未找到
500 服务器内部错误
'''
#01 return 字符串,状态码 这种方式 可以返回不存在的状态码 前端依然能得到页面
@app.route('/status')
def status():
    # 用这种方式可以返回假的状态码 前端依然能够渲染
    return 'hello status',999

#02 利用abort(状态码) 进行返回状态码,只能写入真的状态码
# 这个函数的作用是 自定义我们项目的 出错页面
@app.route('/abort')
def geive500():
    abort(500)

'''
4 捕获访问我们flask后台发生各种错误的情况
    利用@app.errorhandler(500) 进行装饰 能截获500的response
'''
# 捕获500异常 函数当中接受到错误信息
@app.errorhandler(500)
def error500(e):
    return "您请求的页面后台发生错误!错误信息:%s"%e
@app.errorhandler(404)
def error404(e):
    return "您访问的页面飞去了火星!信息:%s"%e

'''
5 重定向
有两种方式:
    01 redirect(url)
    02 url_for(视图函数)
'''
@app.route('/redirect')
def redir():
    return redirect('http://www.baidu.com')


'''
6 url正则
两个用途: 限制访问 和 优化访问路径
使用:
01首先要 定义一个继承自BaseConverter的子类
    在子类里面调用父类的初始化方法
    重写父类的变量
02然后 给applurl_map.converters 字典添加re健 和 我们自己写的类做val

03最后 视图函数的app.route('路径<re(正则),变量名>')      
    变量名要传给视图函数做参数
'''
# 01 写一个继承自 BaseConverter的子类 相应的方法和属性要重写
class Regex_url(BaseConverter):
    def __init__(self,url_map,*args):
        super(Regex_url,self).__init__(url_map)
        self.regex = args[0]
# 02 添加re映射
app.url_map.converters['re'] = Regex_url
# 03 正则匹配参数
# 利用正则对传入参数进行限制
# 只有1到3位小写英文才能成功 否则都是404
@app.route('/attr2/<re("[a-z]{1,3}"):attr>')
def attr2(attr):
    return "hello %s"%attr


'''
7 设置cookie 和 获取 cookie
设置cookie:
    利用 make_response() 拿到response对象
    response.set_cookie(key,val)
获取cookie:
    利用request.cookies.get(key) 获取cookie
'''
# 设置cookie
@app.route('/set_cookie')
def setCookie():
    response = make_response('设置cookie')
    response.set_cookie('log','设置的cookie')
    return response

# 获取cookie
@app.route('/get_cookie')
def getCookie():
    log = request.cookies.get('log')
    return log


if __name__ == '__main__':
    # 执行后台服务器
    app.run(debug=True)