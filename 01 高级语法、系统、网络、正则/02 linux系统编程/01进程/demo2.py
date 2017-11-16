#coding:utf8
'''
python 当中 使用封装好的 multiprocessing 为我们实现创建多进程任务。  

1 Process()方法创建子进程

    使用multiprocessing.Process() 方法产生一个子进程
    基本过程如下：
'''
from multiprocessing import Process
import os
from time import sleep
# 1 指定一个功能，绑定给子进程去完成
def proc_fun(age ):
    sleep(3)
    print("我是子进程%s,age=%s"%( os.getpid() , age ) )

if __name__ =="__main__":
    # 2 创建一个进程实例对象
    #Process()  接收target 代表绑定要完成的函数，不绑定默认执行run方法，第二个元组是传入置顶函数的参数列表，
    #       还可以选择性传参 name代表新建的子进程名字，还可以传入一个字典
    p = Process( target=proc_fun ,args=( 18, ),name="哈哈1号子进程"  )
    # 3 用start() 方法将进程创建出来并且运行
    print("子进程开始执行。。。。")
    p.start()
    print("子进程已开启%s。。。。"%p.name)
    print("开启阻塞收集。。。")
    p.join()#用join（）方法回收子进程的资源，可以传入参数多久后回收
            # 默认是阻塞回收，代表运行完成后再回收该进程的资源 等待期间主进程不继续向下进行
    print("收集结束")





'''
2 创建多个子进程的垃圾回收：
    父进程可以生成子进程，子进程再生成子进程，局面很混乱
    因为子进程的资源回收全是父进程接管的。如果父进程没有回收资源，那么子进程就会丢给1号pid的进程去管理
    所以我们大量生成子进程的时候，要用父进程去生成，然后用父进程进行回收子进程的资源
'''
from multiprocessing import Process
import os

# 1 定义一个子进程需要完成的功能
def proc_fun( num ,m ):
    print("我是子进程%s,我是第%s号被创建的 m=%s"%(os.getpid(),num , m))
if __name__ == "__main__":
    # 2 声明一个子进程的对象,循环调用 用一个父进程生成多个子进程
    jobs = []
    for i in range(10):
        p = Process(target=proc_fun , args=(i,) ,kwargs={ "m":15 })
        p.start()
        jobs.append(p )

    print("进程开启结束，下面进行收集资源")

    for job in jobs:
        job.join()
        print("已经释放了：%s"%(p.name ) )




'''
3 Process函数常用的参数、属性:

    Process语法结构如下：
    
    Process([group [, target [, name [, args [, kwargs]]]]])
    
    target：表示这个进程实例所调用对象；
    
    args：表示调用对象的位置参数元组；
    
    kwargs：表示调用对象的关键字参数字典；
    
    name：为当前进程实例的别名；
    
    group：大多数情况下用不到；
    
    Process类常用方法：
    
    is_alive()：判断进程实例是否还在执行；
    
    join([timeout])：是否等待进程实例执行结束，或等待多少秒；
    
    start()：启动进程实例（创建子进程）；
    
    run()：如果没有给定target参数，对这个对象调用start()方法时，就将执行对象中的run()方法；
    
    terminate()：不管任务是否完成，立即终止；
    
    Process类常用属性：
    
    name：当前进程实例别名，默认为Process-N，N为从1开始递增的整数；
    
    pid：当前进程实例的PID值；

'''






'''
4 用类来实现创建进程对象：
    我们可以定义一个类，继承Process
    实例化一个对象的时候，就会创建一个子进程
    关键点是重写父类的run方法 调用start的时候默认调用run方法
'''
from multiprocessing import Process
# 自己写一个类 继承在Process
class Proc( Process ):
    #实际上在调用子进程的start() 的时候，默认会执行run() 方法
    #  所以要把主要的逻辑写在run方法当中
    def run(self):
        self.sing()

    def sing(self):
        print("正在唱歌！。。。")


if __name__ == "__main__":
    p = Proc()
    print("子进程开始执行：")
    p.start()
    p.join()

