'''
== 与 is ：
is： 比较两个变量的引用是不是一样
    也可以理解成 两个元素的id（） 是不是一样的o
==：当比较的内容是 python中存在的类型，比较的是 值是否一样
    当比较的是类、pythonn中原本没有 我们自己编写的，
        类里面属性特别多，不知道要比较什么，所以默认会采用is的方式进行比较
    当类对象进行 ==  的时候 实际上是调用了 __eq__(self,obj2) 方法
'''
l1=[1,2,3]
l2=[1,2,3]
print( l1 == l2 ) #true 值是相等的
print(l1 is l2)  # False 引用是不同的

print("-"*50)

a=5
b=5
print(a==b) #true  值相同
print(a is b) #true  python中-5到256的小整数常驻内存，不会被消亡 实际上引用是相同的

print("-"*50)
'''
当运 类 对象进行 == 比较的时候， 实际上，调用了 __eq__() 函数
'''
class Person(object):
    def __init__(self, name):
        self.name = name

p1= Person("a")
p2= Person("a")
print( p1 is p2 ) #false
print( p1 == p2 ) #false


class Dog(object):
    def __init__(self, name):
        self.name = name
    def __eq__(self,other):
        return self.name == other.name

d1=Dog("d")
d2=Dog("d")
print(d1 == d2) #true  调用了eq 函数
print(d1 is d2) #false 引用不同