import requests
'''
利用 requests.utilis.dict_from_cookiejar( cookie ) 能够将 cookie转化成字典
利用 requests.utils.cookiejar_from_dict(dict_cookie) 能够将字典转换为cookie
用 response.cookies  能够获取cookie
'''

response = requests.get('http://www.baidu.com/')

# 获取cookie
cookie_jar = response.cookies
print( cookie_jar )

# cookie对象转换成字典
dict_cookie = requests.utils.dict_from_cookiejar( cookie_jar )
print(dict_cookie)

# 字典转换成 cookie
cookie_jar = requests.utils.cookiejar_from_dict(dict_cookie)
print(cookie_jar)