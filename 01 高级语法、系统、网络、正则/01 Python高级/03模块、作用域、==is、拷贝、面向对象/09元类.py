'''
元类就是类的类，
python当中一切都是对象，类也是对象
创建类的 就是元类
'''
a=1
print(type(a))
print(type(type(a)))
def fun():
    pass
print(type(fun))
print(type(type(fun)))
class Foo(object):
    pass
print(type(Foo))
print(type(type(Foo)))
'''
可见type 就是元类
下面我们学习一下 用type()函数创建一个类
用法： type("类名",(继承的类元组)，｛拥有的属性和方法的字典｝  ) 返回一个类对象的引用
'''
#我们用type来创建一个狗类

@classmethod
def bark(cls):
    print( "%s,汪汪！！"%cls.name )
#元组中加,的原因是 一个元素如果不加, 元组默认变成里面元素的类型
Dog = type( "Dog",(object,) , { "name":"大黄","bark":bark } )

dog = Dog()
dog.bark()


