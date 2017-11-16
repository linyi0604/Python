#coding:utf8
''''''
'''
python 是一门动态语言，特性是 能够在执行的过程中更改之前的代码结果

比如 我们完全可以在类和对象先创建之后再给类和对象添加方法和属性

'''

class Animal(object):
    def __init__(self , name):
        self.name = name

dog = Animal("豆豆")

print(dog.name)

'''
给类添加类变量的方法：
'''
Animal.num = 0
# 能够看出来 添加了类属性
print(Animal.num)
print(dog.num)

'''
添加类方法
'''
@classmethod
def classMethod(cls):
    print('类方法',cls.num)
Animal.classMethod = classMethod

@staticmethod
def staticMethod():
    print( "静态方法" )
Animal.staticMethod = staticMethod
#通过这种方式能给类添加静态方法和类方法
Animal.classMethod()
Animal.staticMethod()


'''
添加对象属性
'''
dog.type = "dog"
#这样成员就具有了自己的属性
print(dog.type)

'''
添加对象方法，
    因为对象的方法 需要串参数 self， 这里和不同的绑定不一样，
    自己写的方法不能让对象变量调用的时候自动把self传进去 
    需要用到types.MethodType()来帮助
'''
def printName(self):
    print(self.name)

#添加成员方法
import types
#用这个工具 告诉对象这个是成员方法 调用的时候把self传进去  传入参数 方法和对象进行绑定
dog.printName = types.MethodType( printName, dog )
dog.printName()


'''
删除类和对象的变量和方法
del 对象.属性
delattr(对象 , 属性)
'''
del dog.type

delattr(Animal , "num" )
#print(dog.type)
#print(Animal.num)