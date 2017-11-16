'''
python是一门动态语言，与其他静态语言不同，已经声明的类或者对象，可以在后期添加或者删除属性和方法
'''
#这是一个什么都没有的类
class Person(object):
    pass
#一个实例对象 什么都没有
p1 = Person()

#添加类属性：
print("添加类属性:"+"-"*50)
Person.name="张三"
print(Person.name)
print(p1.name)
#添加成员属性
print("添加对象属性:"+"-"*50)
p1.age=18
print(p1.age)
#添加类方法：
print("添加类方法:"+"-"*50)
#在外部编写函数，在利用类对象添加
@classmethod
def cls_fun(cls):
    print("cls_fun")
@staticmethod
def static_fun():
    print("static_fun")

Person.clsFun = cls_fun
Person.staticFun = static_fun
Person.clsFun()
Person.staticFun()

#添加实例对象方法：
print("添加实例对象方法："+"-"*50)
def printName(self):
    print(self.name)
'''
实例对象方法涉及到传入对象本身为参数，所以不能直接通过引用添加
    需要通过绑定方法 将方法和对象绑定
    types.MethodTypes(方法，对象) 返回一个函数引用
'''
import types
p1.printName=types.MethodType(printName,p1)
p1.printName()

'''
删除属性和方法
del 对象.属性
delatra（对象，"属性名"）
'''