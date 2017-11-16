'''
进程是资源分配的基本单位
线程是cpu调度和分派的基本单位

线程共享进程的资源  进程之间相互独立
多线程的调度 占用资源少 速度较快，但是共享数据不安全
多进程调度 占用资源多，速度较慢


利用threading模块的Thread 开启一个线程

'''
from threading import Thread, current_thread,enumerate
# 1 线程要完成的目标函数
def sorry(num ):
    # current_rhread() 能够帮助我们获取当前的线程编号
    print("%s 对不起，我错了！我是线程%s"%( num,current_thread().name ))

if __name__== "__main__":
    for i in range(10):
        #与Process用法相似 target绑定任务函数，args是参数列表元组，kwargs传入不定参数，name传入线程名字
        #不指定name 默认是thread 1 2 3
        t = Thread( target=sorry,args=(i, ),name = i )
        t.start()

    #可以用threading.enumerate() 返回一个当前所有线程的列表
    threads = enumerate()
    for t in threads:
        #如果不是子进程 进行清理
        if t is not current_thread():
            t.join()
    print("结束")
