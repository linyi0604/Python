'''
在类当中 定义了对象私有变量 __name  在外部和子类当中都是无法获取的
    如果需要获取 要写 get 和set 方法
'''
'''
手写set和get方法得到私有变量
'''
print("手写set和get方法得到私有变量:"+"-"*50)
class Person(object):
    def __init__( self , name ):
        self.__name=name
    def setName( self , name ):
        self.__name = name
    def getName(self):
        return self.__name
p1 = Person("张三")
print(p1.getName())
p1.setName("李四")
print(p1.getName())

'''
通过运用 变量= property(getter,setter) 方法，能够实现在外部的变量访问
'''
print("property() 函数的使用 获取私有变量:"+"-"*50)
class Person2(object):
    def __init__( self , name ):
        self.__name=name
    def setName( self , name ):
        self.__name = name
    def getName(self):
        return self.__name
    #运用property方法 传入 getter 和setter   返回一个引用，外部调用name后自动选择setter和getter
    name = property( getName ,setName )

p2 = Person2("王五")
print(p2.name)
p2.name="赵四"    #自动调用 setName方法
print(p2.name)      #自动调用getName方法

'''
也可以利用property装饰器获取私有变量 这样更加减少了代码
'''
print("使用property装饰器 获取私有变量:"+"-"*50)
class Person3(object):
    def __init__( self , name ):
        self.__name=name

    #利用property装饰器 装饰一个get方法
    @property
    def name(self):
        return self.__name
    #对set方法进行property.setter
    @name.setter
    def name( self , name ):
        self.__name = name


p3 = Person3("王五")
print(p3.name)
p3.name="赵四"    #自动调用 setName方法
print(p3.name)      #自动调用getName方法