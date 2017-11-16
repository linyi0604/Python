#coding:utf8
''''''
'''
== : 是比较两个对象的值是不是相等
        如果 用==比较自己写的类对象，让python比较内部不存在　我们制造出来的，它不知道哪些属于值，会调用is
is : 是比较两个当对象是不是相同引用
'''
li1 = [1,2,3]
li2 = [1,2,3]
print(li1 is li2)   #False
print(li1 == li2)   #True

#python认为小整数常用 常驻内存，变量复制都是指向同一个引用
#小整数是 -5到256的整数 都会常驻内存
#超出这个范围的大整数，python会分代码块 相同块内值相同的对象实际上指向同一个引用
#       不同代码块的变量赋相同值 会指向不同的引用
num1 = 1
num2 = 1
print( num1 == num2)    #True
print( num1 is num2 )   #True

'''
如果我们自己定义类 创建对象
==比较的时候 python不知道我们的类 值是什么，实际上会调用 __eq__ 方法进行比较 默认这个方法就是调用类似is
'''
class Bar(object):
    def __init__(self , n):
        self.n = n


b1 = Bar(1)
b2 = Bar(1)
print(b1 == b2) #False
print(b1 is b2) #False

class Foo(object):
    def __init__(self , n):
        self.n = n
    def __eq__(self, other):
        return self.n == other.n
f1 = Foo(1)
f2 = Foo(1)
print(f1 == f2) #True
print(f1 is f2) #False