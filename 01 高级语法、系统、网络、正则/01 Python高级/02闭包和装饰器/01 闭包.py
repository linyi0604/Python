'''
闭包： 在外函数内部创建了内部函数，并且内部函数中使用了外部函数的局部变量，这样的函数为闭包函数
'''
'''
闭包在执行中：
    当line1 = line(1,2) 的时候，外函数局部变量被赋值，然后创建了内涵数对象，将内涵数对象返回给line1
        因为内涵数还会继续用到外函数a 和b变量，所以a 和b 被复制后 会被绑定给当前的内涵数对象，然后一起返回给line1
        此时line1指向的函数对象是内涵数 带着 外函数的局部变量绑定在它上面
        这样的函数就是闭包函数
    当line1（10） 时候，实际上是执行了getLine（10） 返回了计算结果
'''


#实现一条直线：y = a * x + b    确定a b   传入x 时求出y值
print("实现一条直线：y = a * x + b    确定a b   传入x 时求出y值:")
def line( a , b ):
    def getLine( x ):
        return a * x + b
    return getLine
line1 = line( 1, 2 )
print(line1(10))




'''
闭包中 内涵数修改外部函数中的变量：
    在闭包函数中，不能够修改外函数绑定在内涵数的闭包变量，只能够拿来用。如果想要修改：
'''
'''
在python3中 用nonlocal 关键字声明变量，表示这个变量不是当前变量空间的局部变量，python会向外变量空间找这个变量
'''
#实现一个计数器
print("python3中 闭包修改外部变量的方法nonlocal:")
#全局变量空间
def count(start = 0):
    #闭包变量空间
    def setCount():
        #内部变量空间
        nonlocal start   #nonlocal 声明表示 这个变量不是自己局部变量空间里的变量，python会向外层变量空间一层一层找
        start+=1
        print(start)
    return setCount

count_test = count(5)
count_test()

'''
在python2中 只能用可变类型变量存储，然后在内部函数中修改这种投机取巧的方法
        （在函数中 是能够修改全局变量中可变类型数据的，
            函数中可以修改全局的list变量，如果修改int变量，函数会自动生成一个局部变量给函数来用）
'''
print("python2 中 闭包修改外部变量的方法 可变数据类型：")
def count(start = 0):
    #闭包变量空间
    list=[start]
    def setCount():
        #内部变量空间
        list[0]+=1
        print( list[0])
    return setCount

count_test = count(5)
count_test()


