#coding:utf8
''''''
'''
类对象的私有变量必须通过内部setter getter方法来获取和修改
使用property属性 可以对setter和getter进行优化
'''

class Bar(object):
    def __init__(self):
        self.__name="John"
    def setName(self , name):
        self.__name = name
    def getName(self):
        return self.__name
    #使用property属性 绑定我们的set和get方法 在外部使用的时候自动帮我们调用
    name = property( getName , setName )
b = Bar()
print(b.name) #自动帮我们调用getName
b.name = "josh"  #自动帮我们调用setName
print(b.name)


#更进一步升级，getter用property装饰  set和方法用相同名称
class Foo(object):
    def __init__(self):
        self.__name = 1
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

f = Foo()
print(f.name)   #自动帮我们调用getter
f.name = 2  #自动帮我们调用setter
print(f.name)