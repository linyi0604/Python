
import functools
def decorator(func):
    #functool模块的wraps函数传入目标函数，他能帮我们把目标函数的所有属性迁移给内涵数
    @functools.wraps(func)
    def inner( *args ,**kwargs ):
        print("装饰器的前置业务逻辑")
        res = func( *args ,**kwargs ) #在这里执行目标函数
        print("装饰器的后置业务逻辑")
        return res
    return inner

@decorator  #这里相当于发生了 dest = decorator( dest )
            # 把目标函数dest传进去给了func，返回来的inner给了dest
def dest(): #之后再执行dest 其实执行了inner
    print("这里是目标函数dest")

if __name__ == '__main__':
    #这是再查看属性的时候 就保持了一致性，wraps帮助我们把目标函数的属性迁移了
    print(dest.__name__) #dest