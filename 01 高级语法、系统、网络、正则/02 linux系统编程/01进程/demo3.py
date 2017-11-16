#coding:utf8
'''
python中的进程池：
    我们可以写出自己希望进程帮助我们完成的任务，然后把任务批量交给进程池
    进程池帮助我们创建进程完成任务，不需要我们管理。


进程池：利用multiprocessing 下的Pool能够创建进程池
Pool(n) 传入一个n能够开一个能容纳n个进程任务的进程池。
        如果不传入参数，或者传入负数 能开一个动态控制大小的进程池

具体的使用方法如下：提醒大家要认真看注释

'''
from multiprocessing import Pool
import os,time,random
#绑定给进程工作的函数
def work(num):
    t1 = time.time()
    print("阻塞%s开始，pid:%s"%( num , os.getpid() ))
    time.sleep(random.random()*2)
    t2 = time.time()
    print("阻塞%s结束，消耗时间%.2f"%( num,t2 - t1 ))

def work2(num):
    t1 = time.time()
    print("非阻塞%s开始，pid:%s" % (num, os.getpid()))
    time.sleep(random.random() * 4)
    t2 = time.time()
    print("非阻塞%s结束，消耗时间%.2f" % (num, t2 - t1))

if __name__ == "__main__":
    # p = Pool(3) #开启一个能开三个任务进程的进程池
    # for i in range(10):
    #     #非阻塞的调用func，第二个参数是进程帮我们调用work的时候调的参数表
    #     #p.apply_async( work , (i,))
    #     #以阻塞的形式产生进程任务，生成一个任务进程，等它执行完出池第二个进程才会闯进进池，主进程一直在这里阻塞等待
    #     p.apply( work,(i,) )
    #     print(i)
    # print("开始")

    p = Pool(50)
    for i in range(20):
        # 非阻塞提交，我们发现，直接丢20个任务给进程池，
        # 主进程就不管了，会继续向下执行代码，进程池帮我们管理，把20个执行完
        p.apply_async(work2, (i,)  )

    for i in range(10):
        p.apply(work , (i, ) )

    #关闭进程池，不再接收其他任务
    p.close()

    # join就是阻塞等待所有任务执行完再继续
    #主进程会卡在这里，等所有进程结束再继续执行
    #一定更要先关闭进程池 才能阻塞等待
    p.join()
    print("结束")