import requests
import json

r = requests.get("https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?os=ios&for_mobile=1&start=0&count=18&loc_id=108288&_=0")
html_str = r.content.decode()

with open('a.txt','w') as f:
    f.write(html_str)

# json.load(文件对象) 把json类型直接拿出来转换成字典
with open('a.txt','r') as f:
    dict_json = json.load(f)

print(type(dict_json))
print(dict_json)

# 字典转换成json字符串 ensrure 设置不转换ascii indent自动换行和缩进
str_json = json.dumps(dict_json,ensure_ascii=False,indent=2)
dict_json = json.loads(str_json)  # json字符串转换成字典

with open('b.txt','w') as f:
    # json.dump(字典，文件对象) 把字典写成json本地文件
    json.dump(dict_json,f,indent=2,ensure_ascii=False)