import multiprocessing
import os
import time

def work():
    print("这里是进程池中的进程%s，我的父进程是%s"%(os.getpid(),os.getppid()))
    for i in range(3):
        print("------%s------"%i)
        time.sleep(0.5)

    return "哈哈哈"

def callBack(args):
    print("-----------call back--------------")
    print("这里是 %s，父进程是%s"%(os.getpid(),os.getppid() ) )
    print("%s"%args)


if __name__ == "__main__":
    print("这里是主进程%s"%os.getpid())
    p = multiprocessing.Pool(4)
    # func执行完了之后，回到主进程 callBack被某个进程在主进程中调用
    p.apply_async( func=work , callback=callBack )

    time.sleep(5)
