'''
当用到变量的时候，python 按照LEGB原则进行搜索变量
L local 局部变量空间
E enclosing 闭包变量空间
G global 全局变量空间
B builtins 内构变量空间

locals() 返回当前python的全局变量空间的变量列表
globals() 返回当前局部变量空间的变量列表
'''

#G global 全局变量空间
a=10
glo = globals()
print(glo)
def log():
    # E enclosing 闭包变量空间
    a=20
    def inner():
        # L local 局部变量空间
        a = 30
        loc = locals()
        print(loc)
        print(a)
    return inner

s = log()
s()