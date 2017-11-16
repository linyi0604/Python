'''
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



