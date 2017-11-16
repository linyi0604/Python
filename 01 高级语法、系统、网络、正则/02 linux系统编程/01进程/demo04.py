#coding:utf8
'''
python中进程的通信：消息队列。


    我们知道进程是互相独立的，各自运行在自己独立的内存空间。
    所以进程之间不共享任何变量。
    我们要想进程之间互相通信，传送一些东西怎么办？
    需要用到消息队列！！

'''
'''
进程之间通过Queue进行通信
这是一个消息队列，
q = Queue(n)   开一个能接收n条信息的队列，不传入默认动态延长

q.qsize() 返回队列中消息的条数
q.empty() 队列是否为空
q.get( block,timeout )  取出消息，block默认为True，表示如果为空 一直等取出为止
                            timeout设置等多久，如果到时间还是空就抛出异常
q.get_nowait() 相当于q.get(False) 如果空 立刻抛出异常


q.put(item,block,timeout) item为向队列传送的内容
                            block默认为True 如果队列满了 就一直等有空位再送进去
                            timeout设置时间 到时间了没送进去就抛出异常
q.put_nowait(item) 相当于q.put(False) 如果满了 立即抛出异常


'''
from multiprocessing import Queue
if __name__ == "__main__":
    q = Queue(3)
    q.put("消息1")
    q.put("消息2")
    print(q.full())
    q.put("消息3")
    print(q.full())

    # 从消息队列取数据 推荐两种方法 1 捕获异常   2  判断

    try :
        q.put("消息4",True , 2)   # 尝试写入，如果满了 2秒后抛出异常
    except:
        print("已经满了，现有消息%s条"%q.qsize())
    try :
        q.put_nowait("消息4")   # 尝试写入 如果满了立即抛出异常
        #相当于q.put(item,False)
    except:
        print("已经满了，现有消息%s条"%q.qsize())

    if not q.full():
        q.put_nowait("消息4")

    if not q.empty():
        for i in range(q.qsize()):
            print(q.get_nowait())




'''
在进程池当中使用Queue 需要使用Manager().Queue()
'''
from multiprocessing  import Manager,Pool
import os
def reader(q):
    print("我是子进程%s，我的父进程是%s，我开始读取消息"%( os.getpid(),os.getppid() ) )
    for i in range(q.qsize()):
        print(q.get())

def writer(q):
    print("我是子进程%s,我的父进程是%s，我开始写消息"%( os.getpid(),os.getppid() ))
    for i in "DongGe":
        q.put(i)


if __name__ == "__main__":
    p = Pool()
    q = Manager().Queue()
    p.apply(writer,(q,))
    p.apply(reader,(q,))
    #关闭进程池 不再接收任务
    p.close()
    #阻塞 等待进程结束，必须在close之后
    p.join()

    print("结束")

