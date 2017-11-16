#coding:utf8

'''
正则表达式单字符匹配：
字符：             功能：
.                 匹配任意1哥字符 除了\n
[]                匹配[]中列举的字符
\d                匹配数字0-9
\D                匹配非数字
\s                匹配空白 空格
\S                匹配非空白
\w                匹配单词字符  a-z A-Z  0-9 _
\W                匹配非单词字符
'''


'''
原始字符串：
'''
import re
mm = "c:\\home\\hello\\"
# 实际的路径需要\字符  但是他是特殊字符 需要转义字符\\才能输出\
print(mm)   #c:\hemo\hello\

# 想得到一个 \ 的时候 需要\\去转义
# 如果用re匹配 \\ 就需要四个\\\\才能争取匹配两个\\
res = re.match( "c:\\\\home\\\\" , mm )
print(res.group()) #c:\home\


# 在字符串前面加上 r 表示原生字符串，  可以按照原本的内容匹配 不需要考虑转义
res = re.match( r"c:\\home" , mm )
print(res.group())  #c:\home











