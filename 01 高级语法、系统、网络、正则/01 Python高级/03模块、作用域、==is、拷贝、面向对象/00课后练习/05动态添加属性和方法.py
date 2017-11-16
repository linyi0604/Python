'''
python 是一门动态语言
    和静态语言的区别是　他可以在类对象定义好之后继续添加
'''
class Person(object):
    pass

p1 = Person()

#添加类属性
Person.name="哈哈"
print(p1.name)
print(Person.name)

#添加成员属性
p1.age=23
print(p1.age)

#添加类方法
@classmethod
def clsMe(cls):
    print("this is clsMe")

@staticmethod
def statMe():
    print("this is staticMethod")

Person.clsMethod=clsMe
Person.staticMethod= statMe
Person.clsMethod()
Person.staticMethod()

#添加对象方法
#因为对象的方法要把对象本身传入函数参数，直接添加引用，参数添加会有问题，
# 所以需要types.MethodType(方法，对象)进行绑定
def printName(self):
    print(self.name)
import types
p1.printName = types.MethodType(printName,p1)
p1.printName()

