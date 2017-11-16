#coding:utf8

import re

# search 方法：
ret = re.search( r"\d+","hahaxixixi99999" )
print(ret.group())      #999999

# findall 方法
ret = re.findall( r"\d+","python=111,c=222,h=333" )
print(ret)      # ['111', '222', '333']

# split 方法：根据匹配进行切割字符串 返回一个列表
ret = re.split( r":| ","info:xiaoming haha 33:popo" )
print(ret)      #['info', 'xiaoming', 'haha', '33', 'popo']

# sub 方法：把取到的数据进行替换
ret = re.sub( r"\d+",'[change]',"www.235.353.33.haha.22.com" )
print(ret)

def add(temp):
    return str(int(temp.group())+1 )
ret = re.sub( r"\d+",add,"www.235.353.33.haha.22.com" )
print(ret)