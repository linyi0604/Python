#coding:utf8
''''''

'''
python在寻找变量的时候 遵循LEGB规则
    L local 内部变量空间
    E enclosing 闭包变量空间
    G global 全局变量空间
    B builtins 内建变量空间

    从内部找寻变量 一直到内建
    如果内部存在要使用的变量 则不会在去外层变量空间查找
    
    globals(): 返回当前全局变量空间的所有变量字典
    locals() ： 返回当前局部变量空间的变量字典
'''

# G global 全局变量空间
num = 1

def outter():
    # E enclosing 闭包变量空间
    num = 2
    def inner() :
        # L local 局部变量空间
        num = 3
        print(locals()) #输出当前局部变量空间的变量字典
        print("inner函数内 num：",num)
    print("闭包变量空间内 num:" , num)
    return inner

print(locals()) #输出当前全局变量空间内变量字典
print("全局变量空间内 num:",num)
inn = outter()
inn()