#coding:utf8
''''''
'''
functools模块里面提供了一些方法
'''
import functools

# 1 partial 偏函数， 能够为我们的函数绑定一些默认值，代替闭包来使用
#还是 直线问题  y= a* x + b

def line( a,b,x ):
    return a* x +b

#帮我们绑定了 y = 1 * x + 2
line1 = functools.partial( line , 1 ,2 )
print( line1(5) )


print("-"*50)

# wrap() 装饰器 帮我们使用装饰器的时候 把目标函数的内部变量拷贝到闭包函数来

def demoDecorator(func):
    '''demo doc'''
    def inner( ):
        '''inner doc'''
        print("first")
        func()
        print("last")
    return inner
@demoDecorator
def login():
    ''' login doc '''
    print("登录")

#我们会发现 装饰器装饰之后 我们想取的原函数内部变量都是闭包函数的
print(login.__doc__)
print( login.__name__ )

#这个时候如果用wrap() 可以帮我们实现 把目标函数的东西全都拷贝到闭包当中
def demoDecorator2(func):
    '''demo doc'''
    @functools.wraps(func)
    def inner( ):
        '''inner doc'''
        print("first")
        func()
        print("last")
    return inner
@demoDecorator2
def login2():
    ''' login doc '''
    print("登录")
#用了 wraps() 我们就把目标函数的变量都带到闭包装饰器当中了
print(login2.__doc__)
print( login2.__name__ )