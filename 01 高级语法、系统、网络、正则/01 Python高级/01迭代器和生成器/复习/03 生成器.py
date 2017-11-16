#coding:utf8
''''''
'''
生成器：生成器generator 是一类特殊的迭代器
    我们可以利用生成器很快的写出一个迭代器
    我们写出生成器后python会帮我们包装，元素位置计数和抛出异常都不用我们自己来自做


生成器有两种实现方式：1 （）内放列表推倒式
                   2 yield 关键字函数
'''

from collections import Generator,Iterator,Iterable

#1 () 内放列表生成式
demoGenerator = ( i for i in range(5) )
print( isinstance( demoGenerator , Generator ) )
print( isinstance( demoGenerator , Iterator ) )
print( isinstance( demoGenerator , Iterable ) )

# python底层帮助我们加上记录元素位置和抛出异常的工作
while True:
    try:
        print(next( demoGenerator ))
    except StopIteration :
        print("捕获异常 输出终止")
        break

print("-"*50)


'''
2 用yield函数 实现生成器
    把想要的数用yield抛出，
    调用next时候，函数执行到yield 把目标抛出之后 函数会暂停 等待下一次next方法 或者 send方法的唤醒
    next方法是接收yield 抛出的关键字
    send方法是传进去一个值 之后再接收下一次yield 抛出的目标
    
    yeild函数的返回值会被封装之后的异常对象接收 存入value里面
'''
#n个斐波那契数的生成器
def fibGenerator(n):
    num1 = 1
    num2 = 1
    for i in range(n):
        msg = yield num1
        if msg :    # 当用send方法唤醒的时候，send的参数会被msg接收
            print(msg , end=" ")
        num1 , num2 = num2 , num1 + num2
    # 迭代过后的返回值 会被封装后抛出的异常接收到， 存在value里面
    return "哈哈哈，迭代结束了"

print( isinstance( fibGenerator(5) , Generator ) )
print( isinstance( fibGenerator(5) , Iterator ) )
print( isinstance( fibGenerator(5) , Iterable ) )

for temp in fibGenerator(20):
    print( temp,end=" " )

print("\n","-"*50)


# next() 方法唤醒yield 返回抛出的值
# send() 方法能往里生成器里传一个值被做yield的返回值
# yield生成器的返回值会被封装后抛出异常拿到 存在value里
fib4 = fibGenerator(4)
print(next(fib4))
print(fib4.send("send传入东西啦"))
print(fib4.send("哈哈又传入东西啦"))
print(next(fib4))
#这次会抛出异常 我们接收一下返回值
try :
    print(next(fib4))
except StopIteration as e:
    print(e.value)

