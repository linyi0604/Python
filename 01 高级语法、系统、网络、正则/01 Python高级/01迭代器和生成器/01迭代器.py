'''
迭代：在for循环中 一个一个取出元素为迭代
可迭代对象: 能够放在for in 循环当中完成迭代的对象
        有__iter__()方法，方法的功能是返回一个迭代器
        iter(可迭代对象)来获取迭代器   相当于 可迭代对象.__iter__()
        next(可迭代对象) 来获取下一个元素 相当于 可迭代对象.__next__()
        
'''
'''
判断一个对象是否是可迭代对象的方法：
isinstance([],Iterable) 方法 返回true false   第一个参数是 要检查的对象 第二个参数是特性
'''
from collections import Iterable
print( isinstance([],Iterable) )
print( isinstance( int , Iterable ))





'''
迭代器：
    特点： 有 __iter__() 方法 功能是取出一个迭代器 也就是自身
            并且有__next__()方法 功能是返回下一个元素
                                当越界的时候 next方法会抛出一个异常StopIteration
        不用生成一大串数据，不占用内存，每次通过计算迭代返回结果
'''
'''
判断一个对象是否是迭代器
'''
from collections import Iterator
print(isinstance([],Iterator))
print(isinstance(iter([]),Iterator))



'''
实现一个迭代器： 小于n的斐波那契数 迭代器
    __iter__() 方法返回一个迭代器 也就是自己
    __next__() 方法 返回下一个元素
'''
class fibIterator(object):
    def __init__(self,n):
        self.num1 = 0
        self.num2 = 1
        self.i = 0
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < self.n :
            self.i+=1
            result = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            return result
        else:
            raise StopIteration

fib = fibIterator(10)
for num in fib:
    print(num,end=" ")

