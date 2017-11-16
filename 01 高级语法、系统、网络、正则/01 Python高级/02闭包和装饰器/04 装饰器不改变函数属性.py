'''
在装饰器进行装饰的时候，实际上改变了原函数的引用，调用的是inner函数
所以 inner函数的__name__和__doc__属性 都不是原来目标函数的属性
这个时候我们可以用functools包下的wraps()函数把Inner中的属性改成目标函数
'''


import functools

def log(function):
    #@functools.wraps(function)
    def inner(*args,**kwargs):
        '''我是inner的文档'''
        print("前操作")
        res = function(*args,**kwargs)
        print("后操作")
        return res
    return inner

@log
def test():
    '''哈哈 我是test1的文档'''
    print("哈哈哈 我的name是test")
#此时输出的 __name__的值和__doc__ 都是inner的
print(test.__name__)
print(test.__doc__)



def log2(function):
    #利用wraps()把function的属性同步给inner函数
    @functools.wraps(function)
    def inner(*args,**kwargs):
        print("前操作")
        res = function(*args,**kwargs)
        print("后操作")
        return res
    return inner

@log2
def test2():
    '''哈啊 我是test2的文档'''
    print("哈哈哈 我的name是test")
#此时输出的 __name__的值和__doc__ 是同步过的
print(test2.__name__)
print(test2.__doc__)

