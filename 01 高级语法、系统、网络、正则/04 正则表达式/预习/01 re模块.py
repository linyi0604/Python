#coding:utf8
#导入re模块
import re

#使用match方法进行匹配操作
# result = re.match( 正则表达式, 要匹配的字符串 )
#如果上一步匹配到数据的话 可以使用group方法来提取数据
#result.group()

'''
re.match 是用来进行正则匹配检查的方法
    若字符串匹配正则表达式
    则match方法返回一个对象，否则返回一个None
    匹配对象具有group方法，用来返回字符串的匹配部分
'''
import re
#传入　正则表达式，要匹配的字符串
#如果匹配成功会返回re对象 否则返回None
result = re.match( "itcast" , "itcast.cn")
print( result.group() )

