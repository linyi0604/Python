'''
变量私有化：
    在类当中 变量设置成 __name 的形式，在类外部和子类当中都无法进行和获取和更改
    实际上 是进行了变量名重整    用_类__name 的形式是能获取变量的
'''
class Foo(object):
    def __init__(self,name):
        self.__name = name

f = Foo("哈哈")
print(f._Foo__name)


'''
但是呢上面的方式是不推荐的
一般推荐我们做getter和setter来获取私有变量
'''
class Bar(object):
    def __init__(self):
        self.__name = ""
    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name = name

b = Bar()
b.setName("xixi")
print(b.getName())


'''
在导入外部包的时候
    在包当中如果把变量设置成 _name  那么在外不是无法获取的
'''

'''
如果把变量名设置成 name_ 没有私有化的作用 一般是防止变量名重复
'''