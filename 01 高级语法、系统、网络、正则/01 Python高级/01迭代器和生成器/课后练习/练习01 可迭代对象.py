'''1 判断是可迭代对象
        可迭代对象是 能够放在for in循环当中，里面必须有一个__iter__()方法 返回一个迭代器
    迭代器: 帮助for in 循环将每个元素一个取出来，并判断是否到头
            里面必须有两个方法
            __iter__() 返回一个迭代器 也就是自己
            __next__() 如果没有越界则返回下一个元素 越界了会抛出StopIterator异常
    for in： 会取出可迭代元素的迭代器中next，如果接收到值就正常遍历 如果接收到异常就抛出知道遍历结束了
    
    不仅仅for循环  可迭代对象还可以放进list() tupe() 等 帮我们生成一个对象
'''
from collections import Iterable
print("检查列表是否可迭代"+"-"*20)
print(isinstance([],Iterable) )
print("检查int是否可迭代"+"-"*20)
print(isinstance(int , Iterable))
#模拟一个可迭代对象
print("自己写一个可迭代对象和迭代器"+"-"*20)
class IterableDemo(object):
    def __init__(self):
        self.list = []
        self.i=0
    def add(self,n ):
        self.list.append(n)
    def __iter__(self):
        return IterDemo( self )
class IterDemo(object):
    def __init__(self,list):
        self.list = list
    def __iter__(self):
        return self
    def __next__(self):
        if self.list.i < len(self.list):
            res = self.list[self.list.i]
            self.list.i += 1
            return res
        else :
            raise StopIteration

obj = IterableDemo()
print( isinstance(obj,Iterable))

