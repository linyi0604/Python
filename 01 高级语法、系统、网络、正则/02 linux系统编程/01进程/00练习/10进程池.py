'''
进程池
'''
import multiprocessing
import os
import time
import random
# 1 一个绑定给进程帮助我们完成的工作函数
def work(num):
    print("%s子进程 %s 开始执行 父进程是%s"%(num,os.getpid(),os.getppid() ) )
    t1 = time.time( )
    time.sleep(random.random()*2)
    t2 = time.time()
    print("%s子进程 %s 结束，消耗时间%.2f"%( num,os.getpid() ,t2-t1) )



if __name__=="__main__":
    p = multiprocessing.Pool(3)
    for i in range(10):
        #以非阻塞的方式向进程池里放进程任务,
        #向进程池抛10个进程之后就不管了，池中3个进程一起执行，10个进程排队，主进程继续向下
        p.apply_async( work ,(i,))
        #以阻塞的方式想进程池里放任务
        #任务进到池中 一个一个进行，一个进行完了下一个才能进行，程序停在这里等执行完才能继续向下
        #p.apply( work ,(i,) )
    print("开始")
    p.close()#关闭进程池 不再接收任务
    time.sleep(10)
    p.join() #阻塞等待，等进程任务执行完毕之后才继续向下进行
    print("结束")