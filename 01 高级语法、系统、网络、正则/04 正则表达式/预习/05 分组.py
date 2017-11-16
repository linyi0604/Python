#coding:utf8
'''
匹配分组：
字符              功能
|                 匹配左右任意一个表达式
(ab)              括号内作为一个整体
\num              引用分组num匹配到字符串
(?P<name>)        分组起别名
(?P=name)         引用别名为name分组匹配到的字符串
'''


import re
# 通过引用分组中匹配到的数据即可，但是要注意是元字符串，即类似 r""这种格式
# \1 代表音乐能够之前的第一个分组
ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html>")
print(ret.group())


#匹配出<html><h1>www.itcast.cn</h1></html>
# \2 引用之前出现的 第二个()内的分组   \1 引用之前匹配的第一个()内的内容
#ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", "<html><h1>www.itcast.cn</h1></html>")
ret = re.match( r"<(\w*)><(\w*)>.*</\2></\1>","<html><h1>hahaha</h1></html>" )
print(ret.group())



#(?P<name>) (?P=name)   匹配出<html><h1>www.itcast.cn</h1></html>
# ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", "<html><h1>www.itcast.cn</h1></html>")
ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>","<html><h1>hahaha</h1></html>")
print(ret.group())


