'''
生成器：是一个特殊的迭代器
        利用生成器　我们可以快速的写一个迭代器完成我们的业务逻辑

生成器有２种生成方法

'''

'''
１　将列表生成式　放在() 当中
'''
'''生成10以内偶数的迭代器'''
generatorDemo = ( 2*x for x in range(11) )
'''
print(type(generatorDemo))
print(next(generatorDemo))
print(next(generatorDemo))
print(next(generatorDemo))
'''
'''
for num in generatorDemo:
    print(num)
'''


'''
2 在一个能够正常完成业务逻辑的函数中用yield抛出想要迭代的元素
    暂停：该函数碰到yield关键字时，该函数会把yield后的元素返回 然后函数暂停，等待下一次唤醒
    唤醒：当next() 或者obj.send() 方法 会唤醒 直到 函数结束 或者 下一次yield关键字
    obj.send()： 这个方法传入参数能够被yield接收存给变量在程序内部可以使用
    return： 函数最后的return 会在函数运行结束之后 被迭代器的异常接收，存入e.value
'''
'''
一个斐波那契数（0 1 1 2 3 5   从第三项开始 每一项是前两项的和） 的生成器
'''
def fibGenerator(n):
    i=0
    num1 , num2 = 0 ,1
    while i <= n :
        msg =  yield num1
        print("接收到send()：%s"% msg)
        num1 , num2 = num2 , num1 + num2
        i+=1
    return "返回值在结束时会被异常接收"

'''前5个斐波那契数'''
fib = fibGenerator(5)
'''
    不传入值的时候 msg接收none   传入值时候会接收
'''
print(next(fib))
print(next(fib))
print(next(fib))
print(fib.send("哈哈哈"))

while True:
    try:
        print(next(fib))
    except StopIteration as e:
        print(e.value)
        break