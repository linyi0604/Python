#encoding=utf-8
'''
fork（） 方法只能在linux和unix中使用。
python实现跨平台 产生一个进程可以使用multiprocessing.Process（ ) 方法产生一个子进程
'''
from multiprocessing import Process
import os
from time import sleep
# 1 指定一个功能，绑定给子进程去完成
def proc_fun(age ):
    sleep(3)
    print("我是子进程%s,age=%s"%( os.getpid() , age ) )

if __name__ =="__main__":
    # 2 创建一个进程实例对象
    #Process()  接收target 代表绑定要完成的函数，不绑定默认执行run方法，第二个元组是传入置顶函数的参数列表，
    #       还可以选择性传参 name代表新建的子进程名字，还可以传入一个字典
    p = Process( target=proc_fun ,args=( 18, ),name="哈哈1号子进程"  )
    # 3 用start() 方法将进程创建出来并且运行
    print("子进程开始执行。。。。")
    p.start()
    print("子进程已开启%s。。。。"%p.name)
    #用join（）方法回收子进程的资源，可以传入参数多久后回收
    #   默认是阻塞回收，代表运行完成后再回收该进程的资源 等待期间主进程不继续向下进行
    print("开启阻塞收集。。。")
    p.join()
    print("收集结束")
