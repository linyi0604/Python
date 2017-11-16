'''
迭代器： 在可迭代对象当中 帮助一个一个取出数据
        里面必有两个方法
            __iter__()返回一个迭代器 也就是自身
            __next__() 判断是否越界 如果没有 就返回下一个元素 如果越界了 就抛出一个StopIterator的异常
        python内建的next(obj) 方法能够获取迭代器的下一个元素　等价于 obj.__next__() 方法
'''
# 一个迭代器
class ListIterator(object):
    def __init__(self):
        self.list = []
        self.i = 0
    def add(self,n):
        self.list.append(n)
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < len(self.list):
            res = self.list[self.i]
            self.i += 1
            return res
        else :
            raise StopIteration


listDemo = ListIterator()
listDemo.add(1)
listDemo.add(2)
listDemo.add(3)

''' 越界会抛出异常 '''
'''
while True:
    try:
        print(next(listDemo))
    except StopIteration :
        print("接收异常终止")
        break
'''


''' 判断抛出异常会终止'''
'''
 for num in listDemo:
     print(num)
'''

'''　next(obj) 等价于obj.__next__()  '''
print(next(listDemo))
print(listDemo.__next__())

