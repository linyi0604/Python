#coding:utf8
''''''
import re
'''
表示字符串：
字符              功能
.                匹配任意1个字符 除了\n
[]               匹配[]中列举的字符串
\d               匹配数字　0-9
\D               匹配非数字
\s               匹配空白　空格　\n \t
\S               匹配非空白
\w               匹配合法的单词字符 a-z A-Z 0-9 和 _
\W               匹配非单词字符串
'''
# . 能够匹配任何一个字符
res = re.search( "a.b","acb" )
print(res.group())

# [ ] 匹配里面出现的 任何一个字符
res = re.search( "a[cde]b","acb" )
print(res.group() )

res = re.search( "a[1-9]c","a5c" )
print(res.group())

# \d能够匹配0-9的数字
res = re.search( "a\dc","a5c" )
print(res.group())

# \D 能够匹配0-9的数字以外
res = re.search( "a\Dc","a@c" )
print(res.group())

# \s 能够匹配空白字符
res = re.search( "a\sc","a c" )
print(res.group())

# \s 能够匹配非空白字符
res = re.search( "a\Sc","a#c" )
print(res.group())

# \w 能匹配一个单词字符
res = re.search( "abc\w","abcf  " )
print(res.group())

# \W 能匹配一个单词字符
res = re.search( "abc\W","abc+ " )
print(res.group())


'''
表示数量：
字符              功能
*                匹配前一个字符 0次以上的重复
+                匹配前一个字符 1次以上的重复
?                匹配前一个字符 0或1次的出现
{m}              匹配前一个字符 出现m次
{m,}             匹配前一个字符 m次以上的重复
{m,n}            匹配前一个字符 m-n 次的重复
'''
# * 能匹配前一个字符0次以上的重复
res = re.search( "a*b*c*","aaaaaab" )
print(res.group())

# + 能匹配前一个字符1次以上的重复
res = re.search( "a+b+c+","aaaaaabbbc" )
print(res.group())

# ? 能匹配前一个字符0次或1次的重复
res = re.search( "a?b?c?","ac" )
print(res.group())

# {m,n}   匹配前一个字符 m-n 次的重复
res = re.search( "ab{1,3}c","abbbc" )
print(res.group())



'''
表示边界：
符号              功能
^                匹配字符串开头
$                匹配字符串结尾
\b               匹配单词边界，\b的另一侧不是 英文 数字 下划线的时候才能匹配
\B               匹配非单词的边界， \B 的另一侧需要是 英文 数字 下划线 才能匹配
'''
# ^ 指定字符串的开头
res = re.search( "^abc","abcdef" )
print(res.group())

# $ 指定字符串的结尾
res = re.search( "abc$","ddddabc" )
print(res.group())

# \b 匹配 单词字符的边界 另一侧是非数字 英文下划线 才能匹配
res = re.search( r"abc\b","abc(  " )
print(res.group())

# \B 匹配非单词字符串的边界 另一侧是单词的合法字符才能匹配
res = re.search( r"\Babc","adabc" )
print(res.group())

'''
匹配分组：
符号              功能
|                 或  表示 出现在|两侧的任何一个规则都能够匹配
(ab)              把()内分成一个组，可以调用group(i) 查看第i组匹配结果 也可以在匹配当中用\num 重复使用第num个组
\num              在使用正则表达式的时候可以用\num 引用同一个表达式之前的分组表达式
(?P<name>)        给分组起别名 
(?P=name)         引用组名为name的分组的表达式内容
'''

# | 表示或的逻辑 两侧任意一个匹配就能够匹配
res = re.search( "a(d|b)c","abc" )
print(res.group())

# (ab) 将正则表达式分组
res = re.search( r"(\D*)(\d*)(\D*)(\d*)(\D*)(\d*)" , "ab12cd34ef56g" )
print(res.group())
print(res.group(1)) # ab
print(res.group(2)) # 12
print(res.group(3)) # cd

# \num 引用之前的分组内容
res = re.search( r"<(\w+)><(\w+)>.*</\2></\1>" , "<html><a>hahaha</a></html>" )
print(res.group())

# (?P<name>)给分组起别名   (?P=name)用组名为name的分组的表达式内容
res = re.search( r"<(?P<t1>\w+)><(?P<t2>\w+)>.*</(?P=t2)></(?P=t1)>" , "<html><a>hahaha</a></html>" )
print(res.group())


'''
原始字符串
字符串前面加上r 表示原始字符串
例如 在表示路径的时候：  原路径： c:\hello\
            如果用字符串url表示 \需要转移   url="c:\\hello\\"
            如果使用原始字符串 则 url= r"c:\hello\"

'''