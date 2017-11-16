import requests
import re
'''
利用 requests.session() 拿到一个session对象
用session 来发送get 或者post 能够帮助我们保存服务器带来的session

'''
session = requests.session() # 实例化一个session类

post_data = {
    "email":"mr_mao_hacker@163.com",
    "password":"alarmchime"
}

headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}


session.post('http://www.renren.com/PLogin.do',data=post_data,headers=headers)

response = session.get('http://www.renren.com/327550029/profile',data=post_data,headers=headers)


# 判断是否登录成功
ret = re.findall('毛兆军',response.content.decode())


print(ret)