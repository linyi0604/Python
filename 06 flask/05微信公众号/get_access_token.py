#coding:utf8
from flask import Flask
import datetime
import json
import urllib
app = Flask(__name__)


#封装
# 辅助设施
class AccessToken(object):
    _access_token = {
        'token':'',
        'expires_in':'',
        'updatetime': datetime.datetime.now()
    }

    # 封装方法
    @classmethod
    def get_access_token(cls):
        if not cls._access_token['token'] or (not datetime.datetime.now()-cls._access_token['updatetime'] ).seconds>6800:
            return cls.__update_access_token()
        else:
            return cls._access_token['token']

    @classmethod
    def __update_access_token(cls):
        # 发送请求获取结果
        url = ''
        resp = urllib.urlopen(url).read()
        resp_data = json.loads(resp)

        # 保存全局唯一票据
        cls._access_token['token'] = resp_data['token']
        return cls._access_token['token']


if __name__ == '__main__':
    print( AccessToken() )
    app.run(debug=True)