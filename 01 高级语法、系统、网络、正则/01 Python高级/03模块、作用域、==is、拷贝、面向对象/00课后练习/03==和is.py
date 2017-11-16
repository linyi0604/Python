'''
==: 判断值是不是相等
    对于python已经存在的数据类型 列表 元组等等，是判断值是不是相等
    对于自己写的类 在调用== 时候python实际上会调用类.__eq__(obj) 方法
is: 判断是不是相同的引用 可以理解成 两个对象的id是不是相同
'''
a = 10
b = 10      #对于小整数 常驻内存栈，变量赋值小整数会不断添加引用 不会开辟新的内存
print( a == b)
print( a is b)

c = [1,2,3]
d= [1,2,3]
print(c == d)
print( c is d)

'''
类的==比较是调用__eq__() 方法
'''
class test1():
    def __init__(self , name):
        self.name = name

t1 = test1("哈哈")
t2 = test1("哈哈")
print(t1 == t2)

'''

'''
class test2():
    def __init__(self , name):
        self.name = name
    def __eq__(self,obj):
        return self.name == obj.name
d1 = test2("哈哈")
d2 = test2("哈哈")
print(d1 == d2)