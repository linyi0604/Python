'''
装饰器： 运用了闭包的原理
        实现对一个函数的前后加一些业务逻辑的功能
'''
#一个比较万能通用，可以接受参数和收到返回值的装饰器
def log(function):
    def inner(*args, **kwargs):
        print("前操作。。。。。。。")
        res = function(*args, **kwargs)
        print("后操作..............")
        return res
    return inner
'''
@log 相当于     login= log(login)
    它实际上是把login指向的函数当作参数传入到log当中，然后log的变量存储了引用，放在inner函数当中执行
    然后再把inner函数返回，此时login存了inner函数的引用，再次调用login时候实际上是调用了inner函数
'''
@log
def login(userName):
    print(userName+"用户登录")
    return userName
print(login("张三"))


'''
装饰器的多层嵌套
'''
def log1(function):
    def inner():
        print("log1前操作。。。。。。。。。。。")
        function()
        print("log1后操作。。。。。。。。。。。")
    return inner
def log2(function):
    def inner():
        print("log2前操作......................")
        function()
        print("log2前操作......................")
    return inner
'''
实际上是 test= log1( log2( test ) )
'''
@log1
@log2
def test():
    print("哈哈 我是test 测试多层装饰器")

test()


'''
进一步提升通用性，某些程序可能只想开头处理 结尾不处理
此时采用三层闭包来实现装饰器
'''
def log3( flag ):
    def log2( function ):
        def inner():
            print("前操作")
            function()
            if flag:
                print("后操作")
        return inner
    return log2
'''
此处实际上是 先log3(True) 返回的函数log2对withTail() 进行装饰
'''
@log3(True)
def withTail():
    print("我有后操作")

@log3(False)
def noTail():
    print("我没有后操作")
withTail()
noTail()

