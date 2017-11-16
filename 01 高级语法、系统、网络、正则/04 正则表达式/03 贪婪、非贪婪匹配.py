#coding:utf8
''''''
'''
\w 能匹配 英文 数字 下划线
\d 能匹配数字
如果进行如下匹配：
"abcd123+456"
用"\w+\d+\+\d7"进行匹配的时候   
第一个\w 会一直匹配到abcd12 为止   把3留给了\d
    这种匹配方式为默认的贪婪模式
    如果向把第一个\w只匹配abcd  把123都留给\d 需要在\w后加一个? 取消贪婪 采用非贪婪
'''
import re
# 默认用贪婪模式 这不是我们想要的
res = re.search( "(\w+)(\d+)-\d+", "abc123-456" )
print(res.group(1))
print(res.group(2))


#采用非贪婪模式 在表达式后加？取消贪婪
res = re.search( "(\w+?)(\d+)-\d+", "abc123-456" )
print(res.group(1))
print(res.group(2))