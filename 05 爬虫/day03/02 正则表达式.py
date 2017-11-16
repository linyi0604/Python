import re

'''
    re.findall(正则，目标字符串) 找到全部匹配 返回列表
'''
res = re.findall(r'a.b','a\nb')
print(res) # .匹配任意字符  但是不能匹配\n
# 如果想要匹配换行，需要DOTALL模式
res = re.findall(r'a.b','a\nb',re.DOTALL)
print(res)

# 如果想要匹配 .  需要转义
res = re.findall(r'a\.b','a.b')
print(res)


'''
re.sub(正则，替换目标，目标字符串，) 将匹配到的部分替换
'''
res = re.sub('\d','.','chuan1zhi2')
print(res)


'''
re.compile(正则) 正则表达式的编译 得到一个对象，利用对象进行正则方法
'''
p = re.compile('\d')
res = p.findall('z1m2m3m4n5')
print(res)