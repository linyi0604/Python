'''
实际上编写 setter和getter 在调用当中很费劲
我们运用python的 property 可以帮助我们外部轻松调用
有两种方法
'''
'''
1 name = property(setter, getter ) 
    在外部 使用name的时候 会自动调用setter或者getter方法
'''
class Person(object):
    def __init__(self):
        self.__name = ""
    def setName(self , name):
        self.__name = name
    def getName(self):
        return self.__name
    #使用property方法 返回一个引用，在外部调用这个引用 自动调用set或者get方法
    name = property(getName,setName)

p1 = Person()
p1.name="xixi"  #实际上调用了 set方法
print(p1.name)

'''
2 用property生成器 自动封装get和set方法
    这个时候get和set函数名要一样 在外部调用的时候使用的就是这个名字
'''
class Person2(object):
    def __init__(self):
        self.__name=""
    @property   #此处用装饰器，装饰一个get方法
    def name(self):
        return self.__name
    @name.setter
    def name(self , name):
        self.__name = name

p2 = Person2()
p2.name="哈哈"    #这里自动调用了get方法
print(p2.name)      #这里自动调用了set方法
