#coding:utf8
''''''
'''
xxx : 共有变量
_xxx: 私有化属性或方法，在模块当中前置单下划线的变量不会被导入
__xxx: 类内的私有属性或方法，不允许在外部访问，实际上是发生了名字重整 为 _类__xxx
__xxx__ :魔法方法或魔法属性 被提供的 不要自己制造这样的名字
xxx__： 没有特殊意义
'''

class Bar(object):
    def __init__(self):
        self.__a = 1

b = Bar()
#类的私有化方法 可以通过重整名字 取出来用
print(b._Bar__a)