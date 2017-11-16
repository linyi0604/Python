#coding:utf8
''''''
'''
在python当中 一切都是对象
当我们定义一个函数的时候，实际上函数名只是拿到这个函数的引用

闭包：
    一个函数内部有一个内涵数，并且内涵数使用了外函数的临时变量，外函数消亡的时候，会把临时变量绑定给内涵数
    这样的函数为闭包

'''
# 一个闭包的实例：
def outter( num ):
    def inner():
        print(num)
    return inner
#demo存取了 outter的返回值 也就是inner函数的引用
demo = outter(1)
#相当于执行了inner函数
demo()

print( "-"*50 )

# 应用： 比如我们要做一个直线方程y = a*x +b  如果a b 固定 给x求y的功能
def line( a,b ):
    def set(x):
        return a*x + b
    return set
#获得了直线 y = 4*x +5
line1 = line(4,5)
print( line1(2))

print("-"*50)

'''
闭包 内部函数修改外部函数的方法：
    情况和函数修改全局变量是一样的。
    全局变量在全局空间
    内外函数之间的变量在闭包变量空间
    内涵数变量在内部变量空间
    内涵数可以使用外部的变量但是不能修改，
    入如果修改 需要加 nonlocal关键字声明 表示这个变量不是当前变量空间 在当前的外部
            python会从当前变量空间一层一层往外找
        在python2中 没有nonlocal， 只能用列表这种不可变类型来提供给内部函数修改的功能
'''
def outter(num):
    def inner():
        nonlocal num    #表示num不在当前变量空间 让python向外找
        num += 1
        return num
    return inner
t = outter(1)
print(t())

#在python2中 只能用不可变类型来实现修改
def outter2(num):
    num=[num]
    def inner():
        num[0]+=1
        return num[0]
    return inner
t2 = outter2(1)
print(t2())