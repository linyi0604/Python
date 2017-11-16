'''
用os.fork()方法能够在主进程中创建子进程
    在子进程当中得到返回值0
    在主进程中得到返回值是子进程的pid
    
    可以调用getpid() 得到自己的pid
    可以调用getppid() 得到父进程的pid
    
孤儿进程： 父进程死掉了的子进程
僵尸进程： 子进程死了 的父进程

在操作系统中 子进程的资源由父进程负责回收
    在父进程中用os.wiat() 回收子进程资源
        返回一个二元组 pid 和 state
        pid是子进程的pid  state是状态 0 代表正常回收负数代表有异常
进程在创建的时候会复制一份和主进程完全一样的资源，他们各自拥有自己的变量互不影响
    并且子进程会在fork()方法返回值继续向下运行
'''
'''
os.fork() 只能在类unix系统中运行 windows 不支持
'''
import os

num = 0
pid = os.fork()

if pid == 0:
    print("这里是子进程%s，我的父进程是%s"%( os.getpid(),os.getpid() ))
    num+=1
    print("子进程中num是%s"%num)
else :
    print("这里是主进程%s，我创建了子进程%s" %( os.getpid(),pid ))
    num += 1
    print("主进程中num是%s"%num)
    os.wait() #阻塞等待创建的子进程结束之后回收垃圾的工作
    print("回收完毕")