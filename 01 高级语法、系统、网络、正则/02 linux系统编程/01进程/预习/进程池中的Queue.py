'''
使用Pool创建进程池 需要使用multiprocessing.Manager().Queue()的消息队列
'''
#进程池中的进程通信:

from multiprocessing import Manager,Pool
import os ,time ,random

def reader(q):
    print("%sreader启动，父进程为%s"%( os.getpid(),os.getppid() ))
    for i in range(q.qsize()):
        print("从队列中得到消息%s"%q.get(True))

def writer(q):
    print("%swriter启动，父进程为%s"%(os.getpid(),os.getppid()))
    for i in "DongGe" :
        q.put(i)

if __name__ == "__main__":
    print("父进程%s启动"%os.getpid())
    q = Manager().Queue() #使用Manager中的Queue初始化
    po = Pool()
    #用阻塞的方式去执行进程 write写完了在read
    po.apply( writer, (q,) )
    po.apply( reader, (q,) )
    #关闭队列池子不再接收进程任务
    po.close()
    #等待进程池结束
    po.join()
    print("通信结束%s"%os.getpid())
