'''
python的垃圾回收机制：
    引用计数：优点：节省统一清理内存的时间
                缺点：每个变量维护引用占内存
                        无法解决循环引用问题
    分代收集： 为了进一步解决循环引用问题

python中，以引用计数为主
            分代收集为辅
        引用计数：每当引用计数为0的时候，就把它清楚释放
        分代收集：python中一共有0、1、2  共3代变量收集链表。
                python定时查看0代链表，找到其中引用数量为0的把它释放
                    发现有循环引用的情况并且没有其他引用的时候。把他们的引用计数-1
                    在一轮检查之后还有引用的变量放入1代链表中
                0代链表检查n次后 检查一次1代链表 
                    将循环引用的并且没有其他引用的对象计数-1
                    查询寻一轮后还有引用的 放入2代链表
                1代链表检查n次后 检查2代链表
变量引用计数+1的情况：  对象被创建 a = 1
                            对象被引用 b = a
                            对象被作为参数传入函数 func(a)
                            对象作为一个元素存储到容器中 a = [1,2]
变量引用计数-1的情况：   对象被销毁    del a
                        对象的别名被赋予新的值
                        对象离开作用域
                        容器中被销毁
        
'''
'''
1引用计数： python中每个变量都同时存着引用的数量。当引用数量变成0的时候python就会把这个变量删除，释放内存
'''
'''
1.1 小整数对象池：
    在-5到256之间的数，python认为是常用的，他们会常驻内存当中。当变量赋值在这范围内，引用数量就会增加，
        不论定义多少个变量 他们都指向同一个对象
'''
a=5
b= 5
print(a is b)   #true

'''
1.2 大整数对象池： 
    当变量数值是超出小整数的范围的时候，
    会分程序块。同一块的变量有相同值的时候会使用相同的引用
'''
class Foo(object):
    a = 10000
    b = 10000

class Bar(object):
    a = 10000
    b = 10000

print(Foo.a is Foo.b)   #true
print(Foo.a is Bar.a)   #false

'''
intern机制：当声明字符串变量的时候，如果字符案串没有空格，多个变量字符串值相同，其实会使用相同的引用
'''
str1 = "hello"
str2 = "hello"
print(str1 is str2)    #true
str3 = "hello world"
print(str3 is str2)     #false


'''
查看一个对象的引用计数：
    sys.getrefcount(a)
'''
import sys
m = 999
print(sys.getrefcount(m))

'''
产生内存泄漏：
import gc

class ClassA():
    def __init__(self):
        print('object born,id:%s'%str(id(self)))

def f2():
    while True:
        c1 = ClassA()
        c2 = ClassA()
        c1.t = c2   #产生循环引用
        c2.t = c1
        del c1
        del c2
        #gc.collect() #手动调用垃圾回收机制

#python默认是开启垃圾回收的，可以通过下面代码来将其关闭
gc.disable()    #关闭python的垃圾回收机制

f2()
'''

'''
启动垃圾回收机制 当达到阀值的时候
用下面方法能够获取阀值
返回一个三元组，代表 0代检查多少次后检查1代
            1代检查多少次后检查2代
'''
import gc
print(gc.get_threshold())