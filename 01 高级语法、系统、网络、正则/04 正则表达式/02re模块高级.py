#coding:utf8
''''''
import re
# search()  传入两个参数 reg 和 str   对str从左向右搜索 只要有满足就匹配出来
ret = re.search( "\d+" , "hahah1234" )
print(ret.group())


# match() 传入 reg和str 对str从左边第一位开始匹配 如果不匹配就抛出异常
ret = re.match( "haha" , "hahah1234" )
print(ret.group())

# 会报错   str的第一个字符就不匹配
# ret = re.match( "haha" , "ahahah1234" )
# print(ret.group())

# findall() 函数 传入reg和str  在str只要有符合reg的全都抓出来生成列表返回
list = re.findall( "\d+" , "abc=111,dd=222,f=333" )
print(list)     #['111', '222', '333']

# split() 函数 传入reg和str  对str符合reg规则的进行分割 分割之后各部分放进列表返回
list = re.split( "\D" ,"123d234_2312.23+23" )
print(list)     #['123', '234', '2312', '23', '23']


# sub() 传入三个参数 reg func str  在str找到符合reg的都用func规则处理
def func(a):
    return str( len(a.group()) )

res = re.sub( "\d+", func ,"abc123abc1234abc11abc444" )
print(res)      #  abc3abc4abc2abc3







