'''
异步操作，进程的回调，
运用进程池，apply_async() 提交任务的时候，指定 callback=   回调函数，会在func任务执行结束之后，传送参数给主进程去调用callback
'''

import multiprocessing
import time
import os



def funcTest():
    print("子进程%s哈哈哈，任务,我的父进程是%s"%(   os.getpid(), os.getppid() )  )
    time.sleep(3)
    print("子进程%s哈哈哈，结束"%os.getpid())
    return "哈哈哈"


def callBackTest( a ):
    print("这里是回调函数%s"%os.getpid())
    print( a )




if __name__ == "__main__":
    print("主进程%s"%os.getpid())

    p = multiprocessing.Pool(3)
    p.apply_async( func = funcTest , callback = callBackTest )

    time.sleep(5)
    p.close()
    p.join()

    print("主进程%s" % os.getpid())