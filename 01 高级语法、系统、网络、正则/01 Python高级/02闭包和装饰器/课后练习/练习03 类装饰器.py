'''
类装饰器：其实对类名() 进行调用的时候，会调用类.__call__() 
    所以装饰器的主要逻辑要写在call函数当中
'''
#写一个类装饰器
class log(object):
    def __init__(self,func):
        self.func = func
    def __call__(self):
        print("前操作。。。。。")
        self.func()
        print("后操作、、、、、、、、")

@log
def test():
    print("类装饰器测试函数")


test()