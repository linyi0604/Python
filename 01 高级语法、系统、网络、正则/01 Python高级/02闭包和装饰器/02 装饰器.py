'''
装饰器： 利用闭包的原理，形成对某个函数的处理过程，能够为某个函数的前后实现执行某些代码

额外知识： import time  
    time.ctime()能够返回一个系统当前年月日时分秒的字符串
    time.time() 时间戳，能够返回一个浮点数，是从之前的某个时刻到现在的秒数
    time.localtime(t) 传入一个时间戳，返回一个当前年月日的具体信息的元组
'''

'''实现在某个业务前后分别取一下时间：'''
# 1_定义一个装饰器，实现在调用一个目标函数前后分别输出时间戳
print("1_定义一个装饰器，实现在调用一个目标函数前后分别输出时间戳:"+"-"*20)
#装饰器中必须把目标函数当成参数传进来
import time
def log( function ):    #传入一个函数，这个函数的引用会被保存下来
    def inner():
        print(time.time())
        function()          #目标函数被参数传入，此时执行　前后编写装饰的内容
        print(time.time())
    return inner    #将生成的适配器引用返回
#装饰器的使用，＠函数
        #相当于　login = log( login )  将目标函数的引用传入log，log拿到后　用参数保存了引用，然后将生成的装饰器引用给了原变量login
        #此时的login就已经不是当初的login了，现在它保存着经过修饰的内部函数的引用。内部函数的function保存着目标函数的引用
@log
def login():
    print("模拟实现一个登录功能！")

#此时再调用login()的时候，调用的就已经是装饰器为我们装饰过的了
login()

# 2_多层装饰器的实现与原理
print("2_多层装饰器的实现与原理:"+"-"*20)
#在定义一个装饰器
def log2(function):
    def inner():
        print("log2装饰器开始")
        function()
        print("log2装饰器结束")
    return inner
'''
3_两层装饰器：　
    实际上　是logout = log2(   log( logout )    )
    先看内层，将logout本来的目标函数引用被参数function保存，在inner中执行。inner函数引用返回给logout保存
    此时的logout已经被log装饰器装饰过了，这个时候　logout再被log2装饰
    此时　被log装饰过的logout传入log２引用被function保存放入inner中返回引用给logout　　这是logout已经被两层装饰过
'''
print("3_两层装饰器"+"-"*20)
@log2
@log
def logout():
    print("模拟登出功能！")
logout()

# 4_带参数的装饰器
print("4_带参数的装饰器:"+"-"*20)
'''
当我们对一个函数进行装饰的时候，实际上　目标函数的变量被装饰后实际上保存了inner函数的引用
所以　当我们再调用装饰后的目标函数的时候，实际上调用的是inner函数，　
如果目标函数定义了参数，但被装饰后，再调用，实际上调用了inner函数，　传入参数是接收不到的，产生了问题
所以当目标函数需要传参的时候　需要下面的方法编写装饰器：
'''
def log3(function):
    def inner(*args, **kwargs):     #装饰器需要装饰的目标函数不一定都会传入参数，为了装饰器的通用性，要定义不定参数类型
        print("do log3")
        function(*args, **kwargs)
        print("finish log3")
    return inner
@log3
def rush(x,y):
    print("x和ｙ的和是:%d"%(x+y))
@log3
def test3():
    print("不需要传入参数")

rush(1,2)
test3()

'''
 5_有返回值的装饰器:
    和参数装饰器问题是一样的。我们的目的是写一个装饰器具有很高的复用性，各种各样的函数都可以用它装饰，
    所以我们能能传参数　也能不传参数
    能返回值也可以没有返回值
'''
print("5_有返回值的装饰器:"+"-"*20)
def log4(function):
    def inner(*args,**kwargs):
        print("do log4")
        res = function(*args,**kwargs)
        print("finish log4")
        return res
    return inner
@log4
def test4(x,y):
    return x+y

print(test4(1,2))

'''
6_更高级的通用性：
    比如有些函数希望在结尾时不处理　有些希望在结尾时处理
    此时需要三层闭包嵌套
'''
print("6_更高级的通用性：结尾是否装饰？"+"-"*20)

def log5( flag ):
    def log(function):
        def inner(*args , **kwargs):
            print("前检测")
            res = function()
            if flag :
                print("后检测")
            return res
        return inner
    return log

#此时相当于，将log5的flag局部变量赋值为True后，将flag绑定给log 返回 去给 目标函数进行装饰
@log5(True)
def test5_1():
    print("哈哈 我有后检测")
#此时相当于 将False传入log5的flag后 将flag绑定给内部log返回 为目标函数进行装饰
@log5(False)
def test5_2():
    print("哈哈哈 我没有后检测")
test5_1()
test5_2()
