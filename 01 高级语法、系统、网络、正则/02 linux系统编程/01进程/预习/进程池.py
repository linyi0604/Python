'''
进程池： 利用myltiprocessing.Pool() 可以开一个进程池

Pool(n)可以指定一个最大进程数，
当有新的请求提交到Pool时候，如果池还没满会创建一个新的进程永爱执行该请求
如果池满了，那么会等待 直到池中有进程结束，才会创建新的进程

'''

from multiprocessing import Pool
import os
import time
import random

#给子进程完成的任务函数
#他会 打印自己的pid  然后睡眠n秒，
def work(msg):
    t1 = time.time()
    print("%s开始执行，pid为%s"%( msg,os.getpid() ))
    #生成一个0到1的随机数
    time.sleep(random.random()*2)
    t2 = time.time()
    print("%s执行完毕，耗时%.2f"%( msg,t2-t1 ))


# if __name__ == "__main__":
#     po = Pool(3)    #定义一个进程池，最大进程数是3
#     for i in range(10):
#         # Pool.apply_async(func,(参数,))
#         #每次循环将会用空闲出来的子进程去调用目标
#         po.apply_async(work ,( i , ))
#     print("开始：")
#     po.close() #关闭进程池，关闭后将不再接收请求
#     po.join() #等待po中所有进程执行完，必须放在close之后
#     print("结束！")

'''
multiprocessing.Pool() ：
    apply_async( func, args, kwds ) 非阻塞的方式创建子进程调用func
            args是调用func的参数元组
            kwds 是关键字桉树
        非阻塞：池内的进程可以同时执行任务
        阻塞： 池内进程排队执行任务，第一个执行完 其他进程才能继续执行
    
    apply(func,args,kwds) 阻塞的方式创建子进程并调用指定任务
        阻塞：创建进程塞进池内，但是一个一个执行任务
    close() 关闭进程池，不再接受新的任务进程
    terminate() 不管任务完没完成 立即停止
    join() 主进程足赛，等待子进程的退出，必须在close() 或terminate() 之后使用
'''

if __name__ == "__main__":
    po = Pool(3)    #定义一个进程池，最大进程数是3
    for i in range(10):
        # Pool.apply_async(func,(参数,))
        #每次循环将会用空闲出来的子进程去调用目标
        #以阻塞的方式去添加任务，一个一个执行
        po.apply(work ,( i , ))
    print("开始：")
    po.close() #关闭进程池，关闭后将不再接收请求
    po.join() #等待po中所有进程执行完，必须放在close之后
    print("结束！")
