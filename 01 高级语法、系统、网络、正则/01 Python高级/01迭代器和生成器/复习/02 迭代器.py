#coding:utf8
''''''
'''
迭代器： 是一个能够为完成迭代功能的对象，
    在for in循环当中 实际上，for取出可迭代对象的迭代器，每次用迭代器帮我们取出下一个元素,
            一直到最后一个元素的时候会接受一个异常 这个时候停止迭代*
    
    实质： 迭代器必须具备两个方法：
            __iter__() 返回一个迭代器 也就是自己
            __next__() 放回当前元素的下一个元素
                如果越界了 则抛出一个异常 StopIteration

obj如果是迭代器 我们可以用 obj.__iter__() 取出它的迭代器 
                        obj.__next__() 取出它的下一个元素
    python也内建了 iter(obj) 方法 帮我们返回 和__iter__()的结果
                  next(obj)     帮我们返回和__next__() 的结果


判断： isinstance( obj , Iterator ) 能够判断obj是不是迭代器对象
'''
from collections import Iterator

print( isinstance( [] , Iterator ) )
print( isinstance( iter([]), Iterator ))


#自己写一个迭代器
class DemoIterator(object):
    def __init__(self):
        self.list=[]
        self.i = 0
    def add(self,value):
        self.list.append(value)
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < len(self.list) :
            res = self.list[self.i]
            self.i+=1
            return res
        else :
            raise StopIteration


print( isinstance( DemoIterator() , Iterator ) )


myList = DemoIterator()
myList.add(1)
myList.add(2)

for temp in myList:
    print(temp)


# 一个生成器的应用 完成一个n以内的斐波那契数的迭代器
# 斐波那契数 1 1 从第3个开始都是前两个数的和

class FibIterator(object ):
    def __init__(self, n):
        self.n = n
        self.num1 = 1
        self.num2 = 1
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i <self.n :
            self.i += 1
            res = self.num1
            self.num1 , self.num2 = self.num2 , self.num1 + self.num2
            return res
        else :
            raise StopIteration

fib = FibIterator(20)
for temp in fib:
    print( temp,end=" " )
