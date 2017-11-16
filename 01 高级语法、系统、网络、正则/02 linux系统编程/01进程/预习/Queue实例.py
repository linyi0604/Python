'''
在父进程当中创建一个子进程，
一个往Queue里些数据
另一个读数据
'''
from multiprocessing import Process, Queue
import os, time, random

#向queue里面写消息，以阻塞的方式，写不进去一直等
def write(q):
    for value in ['A','B','C']:
        print( "将%s写入队列"%value )
        q.put(value)
        time.sleep(random.random())

#从queue里面读取数据
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print("从消息队列中获取:%s"%value)
            time.sleep(random.random())
        else :
            break

if __name__ == "__main__":
    #父进程创建Queue 并传递给子进程:
    q = Queue()
    pw = Process( target=write, args=(q,) )
    pr = Process( target=read  , args=(q,) )

    # 开启写进程
    pw.start()
    #等待pw结束
    pw.join()
    #启动读取进程
    pr.start()
    pr.join()


    print("全部数据读写完毕！")