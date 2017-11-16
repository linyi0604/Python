'''
partial 偏函数 是一种工具，给一个普通函数的参数选择性绑定前几个，生成的对象可以继续向后面的参数赋值
    形成的用法类似闭包的用法
'''
#实现 直线的应用： y=a*x+b

def line(a,b,x):
    return a*x + b

from functools import partial

line1 = partial(line, 1 , 1)
line2 = partial(line, 2 ,1 )
print(line1(10))
print(line2(20))