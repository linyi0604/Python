#coding:utf8

'''
微信公众号的开发:
1 获取参数
2 将参数排序后加密
3 校验参数是否正确
4 业务逻辑
5 返回结果三

'''

from flask import Flask,request,make_response
import hashlib

app = Flask(__name__)

@app.route('/wechat8011')
def wechat_validate():
    token = 'python'
    # 获取参数
    signature = request.args.get('signature')
    nonce = request.args.get('nonce')
    timestamp = request.args.get('timestamp')
    echostr = request.args.get('echostr')
    # 定义列表 进行字典序排序
    data = [token,nonce,timestamp]
    data.sort()
    # 拼接字符串
    data = ''.join(data)
    # 拼接后 sha1加密
    if hashlib.sha1(data).hexdigest() == signature:
        return make_response(echostr)
    else :
        return 'error',999


if __name__ == '__main__':
    app.run(port=8011,debug=True)
