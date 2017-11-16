'''
闭包： 在函数内部定义一个函数，并且内部函数使用了外部函数的局部变量
    外函数结束的时候实际上是返回了内部函数的引用，外函数的局部变量在未来还会被使用，
    所以在外函数消亡的时候，局部变量会绑定给内涵数的引用
'''
'''
实现直线 y= a * x + b
  传入x 得出相应的y
'''
def getLine( a , b):
    def line( x ):
        return a * x + b
    return line

line1 = getLine(1,2)
y1= line1(10 )
print(y1 )




'''
闭包的内部函数修改外部函数的局部变量
'''
#python3中需要在内涵数中用nonlocal声明局部变量 表示这个变量不是当前变量空间的变量，python会向上一层变量空间查找变量
#实现一个累加器功能
def count( start = 0 ):
    def set():
        nonlocal start
        print(start)
        start+=1
    return set

coDemo = count(5)
coDemo()
coDemo()
coDemo()


#python2 当中，没有nonlocal关键字， 需要投机取巧，外函数变变量使用可变类型 内部函数技能修改外部变量
#同样一个计数器
def count2( start = 0):
    list = []
    list.append( start )
    def set():
        print(list[0])
        list[0]+=1
    return set

couDemo = count2(3)
couDemo()
couDemo()
couDemo()

