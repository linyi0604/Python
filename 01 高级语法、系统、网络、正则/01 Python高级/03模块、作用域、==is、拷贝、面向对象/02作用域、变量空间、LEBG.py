'''
当python用到一个变量或函数的时候，有搜索这个变量或者函数的范围
遵循LEGB原则
L: local 本地变量空间
E：enclosing 闭包变量空间
G:global 全局变量空间
B：builtins 内构变量空间
globals()函数：能够返回当前全局变量空间的全部属性情况
locals()函数：能够返回当前本地变量空间的全部属性情况
'''
print(globals())

# G global 变量空间
a=100
def enclosing():
    # E enclosing 闭包变量空间
    a=10
    def inner():
        #a=5
        # L local 内部变量空间
        print(locals() )  # locals() 函数能够返会当前局部变量空间的情况
        print(a)
    return inner

func= enclosing()
func()


'''
print() 函数   next() 等内构函数，都是B builtin 内构变量空间提供的
'''