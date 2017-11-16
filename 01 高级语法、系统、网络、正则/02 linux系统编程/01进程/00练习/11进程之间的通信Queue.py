'''
进程之间不共享全局变量，互相通信，要靠Queue消息队列
q= Queue(n) 申请n长度队列，不传n则无限长
q.get() 阻塞取出消息，没有消息就一直阻塞
q.get(True,timeout) 阻塞等待timeout后还没取到就抛出异常
q.get(False)    不等待，消息队列空就抛出异常
q.get_nowait() 不等待，消息队列空就抛出异常

q.put(item) 阻塞传消息，队列满就一直等待
q.put(item,True,timeout) 等待timeout都没传进去 就抛出异常
q.put(item,False)
q.put_nowait() 不等待 队列满就抛出异常

q.full() 检测是否满了
q.enpry() 检测是否空
q.qsize() 返回消息队列中消息的条数
'''

# import multiprocessing
# import time
# import random
# import os
#
# if __name__=="__main__":
#     q = multiprocessing.Queue(3)
#     q.put("消息1")
#     q.put("消息2")
#     print(q.full())
#     q.put("消息3")
#     print(q.full())
#
#     '''
#     在消息队列中读取和传送数据 建议先判断或者用捕获异常
#     '''
#
#     try:
#         q.put("消息4",True,2) #如果队列一直满 2秒后抛出异常
#     except:
#         print("队列消息满了，里面有%s条信息"%q.qsize())
#
#     #用判断的方式读取数据
#     if  not q.full():
#         q.put_nowait("消息4")
#
#     if not q.empty():
#         for i in range(q.qsize()):
#             print(q.get_nowait())

'''
进程之间使用Queue通信的实例
'''
# import os
# import multiprocessing
# def read(q):
#     print("我是读进程%s 开始读取消息。。。" %os.getpid())
#     if not q.empty():
#         for i in range(q.qsize()):
#             print(q.get_nowait())
#     print("读取消息结束")
#
# def write(q,msg):
#     print("我是写进程%s，开始写消息。。。"%os.getpid())
#     if not q.full():
#         q.put_nowait(msg)
#         print("成功写入消息")
#
# if __name__=="__main__":
#     q = multiprocessing.Queue()
#     print("开始")
#     wlist = []
#     for i in range(10):
#         p = multiprocessing.Process( target=write ,args=(q,i) )
#         p.start()
#         wlist.append(p)
#     for p in wlist:
#         p.join()
#
#     p = multiprocessing.Process(target=read,args=(q,))
#     p.start()
#     p.join()
#
#     print("结束")

'''
Queue消息队列在进程池当中的应用
Queue在进程池中使用的时候需要使用 Manger下的Queue
'''
import multiprocessing
import os

def read(q):
    print("我是读进程%s 开始读取消息。。。" %os.getpid())
    if not q.empty():
        for i in range(q.qsize()):
            print(q.get_nowait())
    print("读取消息结束")

def write(q,msg):
    print("我是写进程%s，开始写消息。。。"%os.getpid())
    if not q.full():
        q.put_nowait(msg)
        print("成功写入消息")


if __name__ == "__main__":
    q = multiprocessing.Manager().Queue()
    p = multiprocessing.Pool()

    for i in range(10):
        p.apply_async( write, (q,"哈哈"+str(i)) )

    p.apply_async(read, (q,))

    p.close()   #关闭进程池 不再接收任务
    p.join()    #阻塞等待 一定要在close() 之后









