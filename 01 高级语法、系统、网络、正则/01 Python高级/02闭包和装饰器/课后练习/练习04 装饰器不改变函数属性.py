'''
装饰器装饰函数之后，实际上再次调用的是inner 函数，所以函数对象内的属性全都丢失了
    我们需要把目标函数的属性都拷贝给inner函数才能实现属性的一致
'''

#简单的手动实现
def log(function):
    def inner(*args , **kwargs):
        print("前操作。。。。。。")
        rt = function(*args, **kwargs)
        print("后操作。。。。。。")
        #inner.__name__=function.__name__
        #inner.__doc__=function.__doc__
        return rt
    return inner

@log
def test():
    '''test的说明文档'''
    print("this is test")

test()
print(test.__doc__)
print(test.__name__)



'''
真正的实现需要运用 functools包的wraps()方法 它能够帮我们把目标函数的所有属性都备份过来
'''
import functools
def log2(func):
    @functools.wraps(func)
    def inner():
        print("前操作;;;;;;;;;;")
        func()
        print("后操作。。。。。。。。。。")
    return inner
@log2
def test2():
    '''test2的说明文文档'''
    print("test2..")

test2()

print(test2.__name__)
print(test2.__doc__)
