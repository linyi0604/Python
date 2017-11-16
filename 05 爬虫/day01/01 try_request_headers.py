import requests

#伪装请求头
headers = {
    'User-Agent':'Mozilla/5.0'
}

r = requests.get('http://www.baidu.com',headers=headers)

# print(r.content.decode())


url = 'http://www.baidu.com/'
#get请求的参数
params = {
    'wd':'传智播客'
}
r = requests.get(url=url,headers=headers,params=params)

print(r.content.decode())