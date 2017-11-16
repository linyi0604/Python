#coding:utf8

from flask import Flask,request,make_response
import xmltodict
import time
import hashlib

app = Flask(__name__)

@app.route('/wechat8011',methods=['GET',"POST"])
def wechat_text():
    '''
    获取参数
    校验参数
    构造响应
    返回响应
    :return:
    '''
    if request.method == 'GET' :
        token = 'python'
        # 获取参数
        signature = request.args.get('signature')
        nonce = request.args.get('nonce')
        timestamp = request.args.get('timestamp')
        echostr = request.args.get('echostr')
        # 定义列表 进行字典序排序
        data = [token, nonce, timestamp]
        data.sort()
        # 拼接字符串
        data = ''.join(data)
        # 拼接后 sha1加密
        if hashlib.sha1(data).hexdigest() == signature:
            return make_response(echostr)
        else:
            return 'error', 999

    else :
        # 获取xml格式数据
        xml = request.data
        # 将xml转换成字典 并获取里面数据
        req = xmltodict.parse(xml)['xml']
        # 判断客户端发送的数据类型
        msg_type = req.get('MsgType')
        # 如果接受到的是 text类型 就返回原来接受的
        if 'text' == msg_type:
            resp = {
                'ToUserName':req.get('FromUserName'),
                'FromUserName':req.get('ToUserName'),
                'CreateTime': int(time.time()),
                'MsgType':'text',
                'Content':req.get('Content')
            }
        elif 'voice'==msg_type :
            resp = {
                'ToUserName': req.get('FromUserName'),
                'FromUserName': req.get('ToUserName'),
                'CreateTime': int(time.time()),
                'MsgType': 'text',
                'Content': req.get('')
            }

        else :
            resp = {
                'ToUserName': req.get('FromUserName'),
                'FromUserName': req.get('ToUserName'),
                'CreateTime': int(time.time()),
                'MsgType': 'text',
                'Content': 'Python'
            }
        # 转成xml
        xml = xmltodict.unparse({'xml': resp})
        print(resp.get('Content'))
        return xml

if __name__ == '__main__':
    app.run(port=8011,debug = True)