'''
元类：   类的类
    在python当中一切都是对象 对象是有类生成的，所以说类对象 就是元类创建出来的
'''
a = 1
print(type(a))
print(type( type(a ) ) )


class Foo(object):
    pass

print( type(Foo))


'''
元类 就是创造类的类

我们要使用元类去生成一个类对象

方法： clsName = type("类名"， (继承的类的元组)，｛方法和属性的字典｝  )
'''

@classmethod
def say( cls ):
    print("hello！")

Person = type( "Person" , ( object, ) , {"name": "haha " , "sayHello": say  } )

p1 = Person()
print(p1.name)
p1.sayHello( )


