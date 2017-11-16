'''
为了提高通用性，python提供了multiprocessing模块 根据不同操作系统 调用不同命令创建进程
'''

import multiprocessing
import os
import time
import random
#一个绑定给进程帮我们完成的函数
def work():
    print("%s子进程开始运行"%( os.getpid() ))
    t1 = time.time()
    time.sleep(random.random())
    t2 = time.time()
    print("%s子进程结束，耗时%.2f s"%( os.getpid(),t2-t1 ))

'''
也可以用一个类 继承Process 实现一个对象就是实现一个进程
需要重写run方法
'''
class work2(multiprocessing.Process):
    def run(self):
        print("%s子进程开始运行" % (os.getpid()))
        t1 = time.time()
        time.sleep(random.random())
        t2 = time.time()
        print("%s子进程结束，耗时%.2f s" % (os.getpid(), t2 - t1))

if __name__ =="__main__":
    #开一个列表存储开启的子进程 用来资源回收
    jobs=[]
    for i in range(10):
        #可以传入target指定函数，args指定函数的参数表，kwargs，name等
        #p = multiprocessing.Process( target=work ) #用函数实现target
        #用类实现进程创建
        p = work2()
        p.start()
        jobs.append(p)
    for j in jobs:
        j.join()#阻塞等待 运行结束后回收资源

