'''
集合： 
    存多个不重复值的容器
运算：   交 &      两个集合里都有
        并 |      两个集合所有
        差 -     在a 不在b的
        对称差 ^   a里独有 和 b里都有的并集
'''
z = set("abc")
print(z)
x = set(["x","y"])
print(x)
a = set([1,2,3])
print(a)
b = set([3,4,5])
print(b)

#求交集
print(a & b)
#求并集
print(a | b)

#求差集
print(a-b)

#求对称差 只在a 和只在b的并集
print( a ^ b)