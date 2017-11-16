''''''
'''
迭代：列表 元组 字符串等放在for in 循环当中 一个一个对象挨个取出来 就是迭代
    迭代是只能向前不能向后的

可迭代对象：可以放入for in 循环的进行迭代取出元素的对象都是可迭代对象
    它的本质是里面有一个__iter__ 方法 功能是返回一个迭代器，帮助我们完成迭代功能

判断： 用 isinstance(obj , iterable) 可以判断obj是不是可迭代对象
'''
from collections import Iterable
# 列表 元组 字典 字符串 都是可迭代对象
print( isinstance( [] , Iterable ) )
print( isinstance( "" , Iterable ) )
print( isinstance( {} , Iterable ) )
# 整数不是可迭代对象
print( isinstance( 100 , Iterable ) )


#我们自己定义一个对象是多元素容器 但是他不是可迭代对象
class demoIterable(object):
    def __init__(self):
        self.list = []
    def add(self, value):
        self.list.appnd(value)

print(isinstance( demoIterable() , Iterable ))


# 可迭代对象的实质是 里面必须有一个__iter__方法 功能是返回一个迭代器 这才是一个迭代器
class demoIterable2(object):
    def __iter__(self):
        pass

print( isinstance( demoIterable2() , Iterable ) )