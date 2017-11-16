'''
表示边界：
字符                      功能
^                          匹配字符串开头
$                          匹配字符串结尾
\b                         匹配一个单词的边界
                            \bxxx\b  表示字符串中 出现xxx的地方，左侧和右侧相邻的一个都不是英文字符才能匹配
\B                         匹配一个非单词的边界
                            \Bxxx\B  字符串中 出现xxx的左侧和右侧相邻的一个字符是英文字符才能匹配
'''

import re
#匹配邮箱  合法标识符@合法标识符.com结尾
ret = re.match( "[\w]*@[\w]+(\.com)$" , "fldsjf@qq.com" )
#ret = re.match( r"[\w]*@[\w]+\b.com\b" , "fldsjf@qq.com" )
print(ret.group())


# \b  \B
ret = re.match(r".*\Bcd\B.*" , "abcdefg")
print(ret.group())

ret = re.match(r".*\bcd\b.*" , "ab cd%efg")
print(ret.group())

