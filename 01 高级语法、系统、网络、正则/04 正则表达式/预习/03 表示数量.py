#coding:utf8

'''
表示数量：
字符                      功能
*                        匹配前一个字符出现0 - 无限 次
+                        匹配前一个字符出现1 - 无限 次
？                       匹配前一个字符出现 0 或1 次
｛m｝                    匹配前一个字符出现m次
{m,}                    匹配前一个字符出现至少m次
{m,n}                   匹配前一个字符出现m-n次
'''

import re
# # 匹配一个大写英文之后跟着一个小写
# ret = re.match( "[A-Z][a-z]" , "Mm" )
# print(ret.group())  #Mm


ret = re.match( "[a-zA-Z_]*", "2_name1" )
print(ret.group())


