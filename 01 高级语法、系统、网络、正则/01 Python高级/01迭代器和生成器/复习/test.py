'''
迭代： 可以放入for循环当中 一个一个 把里面数据拿出来 
可迭代对象： 可以for in 循环  是一个容器 包含多个数据 
    实质： 里面有一个__iter__() 方法 返回一个可帮助自己迭代的 迭代器

判断可迭代对象： isinstance( obj , Iterable )
'''
from collections import Iterator , Iterable , Generator
# class Demo(object):
#     def __iter__(self):
#         pass
#
# d = Demo()
#
#
# print( isinstance( d , Iterable ) )

'''
迭代器：  实质： 一定有 __iter__()    返回一个迭代器 也就是自己
                    __next__()      如果没有越界返回下一个元素
                                 如果越界了 抛出 StopIteration 异常
'''
# n 以内偶数的迭代器
#
# class Demo(object):
#     def __init__(self , n):
#         self.n = n
#         self.i = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.i <= self.n :
#             res = self.i
#             self.i +=2
#             return res
#         else:
#             raise StopIteration

#
# d = Demo(10)
#
# for temp in d:
#     print(temp)

# print( isinstance(d,Iterator ))
# d = Demo(10)
# li = list(d)
# print(li)


'''
生成器： 一类特殊的迭代器  他是python 为我们封装好的
        我们只需要 实现业务逻辑，抛出异常都不需要我们自己做 
        python为我们接管了


生成器的两种实现方式：
    1 () 内放入列表推倒式
    2 yield 关键字函数
'''

#1 列表生成式
# gen = ( i for i in range(10) )
# for i in gen:
#     print(i)


# yield关键字函数
#yield关键字函数的生成器
# 一个n以内偶数的生成器
def odd(n):
    for i in range(0,n+1,2):
        '''
        代码的执行从右向左，当遇到yield的时候，会把i抛出给next的调用返回，然后函数停在这里
            下一次外面调用next或者send方法唤醒的时候，msg = 开始执行，上一次停在了yield i 这里，左边还没执行
            然后再碰到yield i 的时候把i抛出来再暂停。。。。。。
        '''
        msg = yield i
    '''
    当函数执行结束的时候python认为迭代器结束了，帮我们抛出异常，返回值会被异常对象接收存在了value属性里面
    '''
    return "哈哈哈"
#用gen获取一个生成器的对象
gen = odd(5)

#生成器也是迭代器，用next方法唤醒yield暂停，继续向下执行
print( next(gen) )#0
print( next(gen) )#2
print( gen.send("传入数据") )#传入数据 4   这个时候 在函数里面会打印出来传入的 “传入数据”， 并返回了下一次的i 也就是4 然后暂停

#这时候不论next还是send，迭代器都已经结束了 python会帮我们抛出异常，函数的返回值会被异常对象接收存在value属性里
try :
    print( next(gen) )
except StopIteration as e :
    print(e.value)      #会打印出 哈哈哈， 也就是odd函数的返回值

