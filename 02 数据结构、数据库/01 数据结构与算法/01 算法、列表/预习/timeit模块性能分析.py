'''
python中内置的 计算代码执行时间的模块
import timeit
t = timeit.Timer( "执行函数", "导入模块" )   获取一个绑定函数执行的对象
t.timeit( number=次数 )  获取执行指定次数的时间

'''



def concat():
    l = []
    for i in range(1000):
        l = l + [i]

def append():
    l =[]
    for i in range(1000):
        l.append(i)

def comprehension():
    l = [ i for i in range(1000)]

def list_range():
    l = list(range(1000))

from timeit import Timer


t1 = Timer("concat()", "from __main__ import concat" )
print("concat", t1.timeit(number=1000),"seconds")

t2 = Timer( "append()" , "from __main__ import append" )
print( "append", t2.timeit(number=1000),"seconds" )

t3 = Timer( "comprehension()" , "from __main__ import comprehension" )
print( "comprehension" ,t3.timeit(number=1000), "seconds")

t4 = Timer( "list_range()" , "from __main__ import list_range" )
print( "list_range" , t4.timeit(number=1000), "seconds" )

print("-"*100)

x = list(range(100000) )
t5 = Timer("x.pop()" ,"from __main__ import x" )
t6 = Timer( "x.pop(0)", "from __main__ import x" )
print( "pop(0)",t6.timeit(number=10000),"seconds" )
print("pop",t5.timeit(number=10000),"seconds")


print("-"*100)


t7 = Timer( "x.append(1)" ,"from __main__ import x" )
t8 = Timer( "x.insert(0,1)","from __main__ import x" )

print( "append" , t7.timeit(number=1000) ,"seconds"  )
print( "insert(0,1)" , t8.timeit(number=1000) ,"seconds"  )
