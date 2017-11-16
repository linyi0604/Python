#coding:utf8
''''''

'''
python当中万物都是对象 
元类就是类的类，是创建一个类的父类
'''
def func():
    pass
print(type(func))
print( type( type( func ) ) )

'''
元类也就是type
利用type创建一个类: type( 类名，( 父类元组 father1,father2 ) ， { 属性字典 key:value } )
'''
import types
def strFunc():
    print("哈哈哈")
Foo = type(
    "Foo",
    ( object ,  ),
    {
        "name":"hahah",
        "printHaha": strFunc
    }
)

print(Foo.name)
Foo.printHaha()

f = Foo()
print(f.name)

print("-"*50)
'''
自定义一个元类函数，调用该函数创建一个类，
    我们自己把传入的属性名改成大写 用以验证我们是否自己模拟实现了一个元类
'''
#我们模拟实现的一个元类
def produceClass( name , fathers , attrs ):
    upper_attrs={}
    for key,value in attrs.items():
        upper_attrs[key.upper()]=value
    return type( name , fathers , upper_attrs )

Foo = produceClass( "Foo" , (object,) , { "name":"小明" } )
print( hasattr(Foo,"name") )
#通过验证 我们自己实现了元类 把属性名改成大写后创建了类
print( hasattr(Foo,"NAME") )
f = Foo()
print(f.NAME)


'''
实现一个元类  我们创建类的时候会使用我们自己写的元类
    实际上 当我们正常的去创建一个类的时候，python会首先查找自己的__metaclass__ 模块方法
        如果自己没有写这个方法，那么会找父类的，，一直这样找上去 一直找到type
        所以 我们自己要实现一个类的元类 就是置顶这个类的__metaclass__
'''

def meta(name, fathers, attrs):
    upper_attrs = {}
    for key, value in attrs.items():
        if key.startswith("__"):
            upper_attrs[key] =value
        else :
            upper_attrs[key.upper()] = value
    return type(name, fathers, upper_attrs)

#在python3中
class Foo( metaclass=meta ):
    f = 1

print( hasattr(Foo ,"f") )  #alse
print( hasattr(Foo ,"F") )  #True


#在python2当中
# class Bar():
#     __metaclass__ = meta
#     b = 1
#
# print(hasattr( Bar , "b" ))
# print(hasattr( Bar , "B" ))


#用一个类来实现元类的功能  创建类的时候继承自我们这个元类
#实际上我们要重写__new__ 方法 这是一个在init之前执行的方法

print("-"*50)


class metaCls(type):
    def __new__(cls , name, fathers, attrs):
        upper_attrs = {}
        for key, value in attrs.items():
            if key.startswith("__"):
                upper_attrs[key] = value
            else:
                upper_attrs[key.upper()] = value
        #return type(name, fathers, upper_attrs)
        #return type.__new__(cls, name, fathers, upper_attrs)
        #return super().__new__(cls ,name, fathers, upper_attrs)
        return super( metaCls , cls ).__new__(cls ,name, fathers, upper_attrs)

#在python3当中
class Foo( metaclass=metaCls ):
    f = 1

print(hasattr(Foo , "f"))   #False
print(hasattr(Foo , "F"))   #True