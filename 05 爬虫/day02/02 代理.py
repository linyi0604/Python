import requests

'''
在发送请求的时候 带上proxies 字典参数，
proxies = {
    '协议':'url'
}

可以制定ip为我们发送请求

'''
proxies = {
    'http':'http://122.193.14.114:83'
}

headers = {
            'User-Agent':'Mozilla/5.0'
}

r = requests.get('http://www.baidu.com',headers=headers,proxies=proxies)
print(r.status_code)