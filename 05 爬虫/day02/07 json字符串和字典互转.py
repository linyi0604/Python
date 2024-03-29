import requests
import json
'''
json.loads(json_str) json字符串转换成字典
json.dumps(dict) 字典转换成json字符串 

'''
# 这是一个ajax发起的get请求，获取一个json对象
r = requests.get("https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?os=ios&for_mobile=1&start=0&count=18&loc_id=108288&_=0")
json_response = r.content.decode()  # 获取r的文本 就是一个json字符串

# 将json字符串转换成dic字典对象
dict_json = json.loads(json_response)
print(type(dict_json))

# 将字典转换成json字符串
str_json = json.dumps( dict_json )
print(type(str_json))

# 字典转换成json 存入本地文件
with open('./a.txt','w') as f:
    # 设置不转换成ascii  json字符串首缩进
    f.write( json.dumps( dict_json,ensure_ascii=False,indent=2 ) )

