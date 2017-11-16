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

class Foo(object):
    def __init__(self):
        self.a= 1
        self.b = 2
    def __getattribute__(self, item):   #当外部尝试获取属性的时候 会调用这个方法
        if item == "a":
            return 10
f = Foo()
print(f.a)


'''
__getattrbute__ 的坑
'''
class Bar(object):
    def __init__(self):
        self.a= 100
    def __getattribute__(self, item):
        if item == "a":
            #在getattribute里面写self获取会陷入死循环 因为每次都会调用这个函数
            #return self.a
            #要回复正常功能，只能借助父类的这个方法 有一下几个方法
            #return super().__getattribute__(item)
            #return super(Bar, self ).__getattribute__(item)
            return object.__getattribute__(self,item)
b = Bar()
print(b.a)