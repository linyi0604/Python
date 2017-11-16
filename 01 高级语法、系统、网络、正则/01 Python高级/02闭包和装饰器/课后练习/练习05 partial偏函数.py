'''
partial偏函数 是一个帮助我们绑定某个函数是前几个参数的工具，得到的对象我们可以像使用闭包那样使用他
上例子：
'''
'''
实现一条直线 y= a*x + b
'''
import functools

def line(a,b,x):
    return a* x + b
#用这个方法得到一个对象 相当于a=5 b = 4  我们只需要对line1 传入x就能得到y值了
line1 = functools.partial(line,5,4)

print(line1(10))