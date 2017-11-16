'''
生成器： 是一类特殊的迭代器
    通过生成器我们能生成一个迭代器
生成器有两种创建方法
'''

# 1 ( 列表推导式 )
#生成前十个偶数的列表
list = [ x*2 for x in range(11) ]
print(list)

#生成前十偶数的生成器
oddIterator=( x*2 for x in range(11))
print(type(oddIterator))
for num in oddIterator:
    print(num,end=" ")

# 2 yield 关键字  当迭代到尽头的时候，函数的返回值会被StopIterator接收存在e.value里面
#生成前n个斐波那契数的迭代器
print()
print("yield关键字创建迭代器"+"-"*20)
def fibGenerator(n):
    num1 = 0
    num2=1
    i=0
    while i < n:
        yield num1
        num1 , num2 = num2 , num1 + num2
        i+=1
    return "结束了"
fib = fibGenerator(10)
for num in fib:
    print(num,end=" ")

print()
print("异常接收返回值"+"-"*20)
fib2 = fibGenerator(5)
while True:
    try:
        print(next(fib2))
    except StopIteration as e:
        print(e.value)
        break;


#2.1  .sent()方法能够向生成器内传送值
print()
print("2.1 generator.sent方法"+"-"*20)
#一个返回n以前的偶数的生成器
def oddGenerator( n ):
    i=0
    while i< n:
        recieve = yield i
        print(recieve)
        i+=1

odt = oddGenerator(10)
#next方法能取迭代器的下一个元素
print(next(odt))
print(next(odt))
print(odt.send("哈哈"))
print(odt.send("呵呵"))



