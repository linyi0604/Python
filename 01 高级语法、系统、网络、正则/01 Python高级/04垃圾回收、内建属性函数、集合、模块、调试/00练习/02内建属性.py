'''
python的内建属性：
    __init__ 构造函数初始化
    __new__ 生成实例所需属性
    __class__ 实例所在类
    __str__ 调用print方法时获取返回值 默认与__repr__相同
    __repr__ 类实例
    __del__ 析构
    __dict__ 实例自定义属性
    __doc__ 说明文档
    __bases__ 所有父类构成的元素
    __getattritbute__ 属性访问拦截器

'''
'''
当从外部获取类属性的时候 实际上是调用了 类的 __getattribute__() 函数。
    如果当前类没有这个函数那么会调用父类的这个函数　一直到 type为止

'''
class Person(object):
    a = 100
    def __getattribute__(self, item):
        if item == "a":
            return 2000
        #这是一个坑　如果没有这个属性，每次用self.xxx 就会无限的进入这个函数没有出口
        else:
            return self.item

print(Person.a)
#print(Person.b)