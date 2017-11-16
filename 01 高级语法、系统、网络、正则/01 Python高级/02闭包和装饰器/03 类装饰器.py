'''
类装饰器： 
对于class而言，也能够写一个装饰器提供装饰作用
当 类名() 操作的时候，其实会调用 类.__call__() 方法
所以实现装饰功能的逻辑在　call里面
'''

#普通装饰器
# def log(func):
#     def inner():
#         print("前操作")
#         func()
#         print("后操作")
#     return inner


#类装配期
class Decorator(object):
    def __init__(self,func):
        self.func = func
    def __call__(self):
        print("类装饰器前操作")
        self.func()
        print("类装饰器后操作")



@Decorator
def login():
    print("login now")

if __name__ == '__main__':
    login()


