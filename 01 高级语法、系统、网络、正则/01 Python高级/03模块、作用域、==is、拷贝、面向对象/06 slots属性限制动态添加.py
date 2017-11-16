'''
python的动态性导致我们可以先编写类 后生成属性和方法
我们如何限制呢
运用__slots__属性可以绑定对象可以拥有的变量和方法，不能多添加
__slots__ 是一个元组，里面是变量或者方法名，写死之后，只能在外面为该对象添加slots里面的属性或者方法
'''
class Person(object):
    __slots__ = ("name","age")

p1 = Person()
p1.name="张三"
p1.age=18
#p1.gender = 2   #这个变量没有写入slots当中，会报异常
print(p1.name)
print(p1.age)
#print(p1.gender)
