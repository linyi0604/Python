#coding:utf8
''''''
'''
装饰器： 利用闭包的原理，实现对要执行的业务逻辑函数前后添加一些固定操作的功能
    一个闭包函数： 外函数接收目标函数，内涵数进行调用
'''
import time
#如果我们要对一个模块计算一下耗费的时间 可以利用装饰器

#装饰器函数
def decorator(func):
    def inner():
        print("登陆前时间：",time.time())
        #在这里执行目标函数
        func()
        print("登陆后时间：",time.time())
    return inner



#一个模拟登录模块的例子 用装饰器装饰
@decorator #相当于 login = decorator( login )
           # login 拿到了inner函数的引用，inner 里面的func就是原来的login函数
def login():
    print("已登录！")

#在这里执行 已经被装饰器装饰
login()

print("-"*50)


#如果我们的目标函数需要传入参数和返回值呢？？我们的装饰器需要修改成通用的
def demoDecorator(func):
    def inner( *args,**kwargs ):
        print("登陆前时间：", time.time())
        # 在这里执行目标函数 如果有参数穿进去 就用内涵数接收 再穿进去  如果需要返回值就会返回 否则返回None
        res = func( *args,**kwargs )
        print("登陆后时间：", time.time())
        return res
    return inner

@demoDecorator
def login2( username ):
    print(username,"登录！")
    return username

res =login2("林奕")
print(res)

print("-"*50)
# 多层装饰器的嵌套：
# 相当于先被内层装饰器 装饰之后 再整个被外层装饰器装饰
def outsideDecorator(func):
    def inner(*args , **kwargs):
        print("外层装饰器前操作")
        res = func()
        print("外层装饰器后操作")
        return res
    return inner

def insideDecorator(func):
    def inner( *args, **kwargs ):
        print("内层装饰器前操作")
        res = func(*args , **kwargs)
        print("内层装饰器后操作")
        return res
    return inner

@outsideDecorator
@insideDecorator
#相当于 login3 =  outsideDecorator( insideDecorator( login3 ) )
# 内层装饰器先装饰 把内涵数引用存在login3 之后再被外层装饰器装饰 相当于 login3存了外装饰器的inner ， 外装饰器的inner里面的func存了内装饰器的inner，内装饰器的func存了目标函数
def login3():
    print("多层装饰器登陆模块")
login3()
print("-"*50)

'''
如果有些函数需要前置操作 不需要后置操作，我们的装饰器 变得更灵活,
    传入一个参数 告诉装饰器要执行哪些装饰，需要三层闭包
'''
def chooseDecorator( flag ):
    def outter( func ):
        def inner( *args, **kwargs):
            print("选择装饰 前操作")
            res = func( *args, **kwargs )
            if flag:
                print("选择装饰后置操作")
            return res
        return inner
    return outter

@chooseDecorator(False)
#相当于 传入False后拿到了 outter 携带一个flag进行装饰
def login5():
    print("选择 装饰器 取消了后置操作")

login5()

print("-"*50)
'''
类实现装饰器：
    当调用类名() 的时候  实际上是调用了类里的__call__ 方法 素以实际上我们需要的是重写call方法
'''
class ClassDecorator( object ):
    def __init__(self,func):
        self.func = func
    def __call__(self ,*args , **kwargs):
        print("类装饰器 前置操作")
        res = self.func( *args , **kwargs )
        print("类装饰器 后置操作")
        return res

@ClassDecorator
def login4():
    print("类装饰器登录模块")

login4()


