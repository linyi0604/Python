#装饰器函数 传入目标函数做参数
def decorator( func ):
    #实际调用目标函数会发生调用inner，
    # 所以我们让inner接收不定参数，我们再把不定参数传给目标函数func
    #这样不论我们传入什么参数目标函数都能接收到！！
    def inner( *args , **kwargs ):
        print("装饰器函数中。。目标函数执行之前的操作！！")
        # 我们设置一个变量接收目标函数的返回值，在inner结束的时候再把返回值返回去
        # python不同于其他语言，即使我们没有编写func的返回值，也会默认返回None，所以这里不会报错
        res = func( *args , **kwargs )
        print("装饰器函数中。。目标函数执行之后的操作！！")
        return res
    return inner
#这样编写的装饰器，在外部看来，我们就可以传入参数给目标函数
# 同时也可以正常接收目标函数返回的参数!!!

@decorator  #实际上会发生 destination = decorator( destination )
            # 把目标函数传入装饰器函数返回了inner给destination
            # 此后我们再调用destination 实际上调用了inner函数的一个对象
def destination( a ):
    print( "目标函数接受到参数:%s"%a )
    return "目标函数的返回值%s"%a

if __name__ == '__main__':
    # 这里实际上调用了inner函数的对象，我们传入参数和接收返回值都没有问题了！
    res = destination(10)
    # 打印一下返回值！
    print(res)
    '''
    执行结果:
        装饰器函数中。。目标函数执行之前的操作！！
        目标函数接受到参数:10
        装饰器函数中。。目标函数执行之后的操作！！
        目标函数的返回值10    '''