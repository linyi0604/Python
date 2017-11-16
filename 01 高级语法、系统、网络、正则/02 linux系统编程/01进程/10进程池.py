'''
进程池：利用multiprocessing 下的Pool能够创建进程池
Pool(n) 传入一个n能够开一个能容纳n个进程任务的进程池。
        如果不传入参数，或者传入负数 能开一个动态控制大小的进程池
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
    #     #非阻塞的调用func，第二个参数是调用时候的参参数元组
    #     #p.apply_async( work , (i,))
    #     #以阻塞的形式产生进程任务，生成一个任务进程，等它执行完出池第二个进程才会闯进进池
    #     p.apply( work,(i,) )
    #     print(i)
    # print("开始")

    p = Pool(50)
    for i in range(20):
        p.apply_async(work2, (i,)  )

    for i in range(10):
        p.apply(work , (i, ) )

    #关闭进程池，不再接收其他任务
    p.close()

    #阻塞等待所有任务执行完再继续
    p.join()

    print("结束")




