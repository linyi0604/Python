#coding:utf8
''''''
'''
python的动态性 让我们可以在运用的时候随意添加变量和方法 
运用slots 插槽 可以限制动态添加属性和方法
'''
class Person(object):
    __slots__ = ( "name", "age" )

xiaoming = Person()
xiaoming.name="小明"
xiaoming.age= 18
print(xiaoming.name)
print(xiaoming.age)

xiaoming.num = 3 #会抛出异常 不允许添加这个属性