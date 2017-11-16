'''
集合set() 一种容器 相同值只能存一个
交集 &
并集 |
差集 -
对称差 ^
'''
a = set([1,2,3])
b = set([2,3,4])
print(a)
print(b)
#a 交 b运算
print(a & b)
# a 并b 操作
print( a |b )
# a - b
print(a-b)
# 对称差
print( a^b)