'''
为了实现任务的并发，我们引入进程的概念

在当前的程序当中，当前程序是一个主进程，
我们用os.fork() 方法能够实现在当前主进程上创建一个子进程

os.fork() 方法有两次返回值
主进程会接收到子进程的pid作为返回值
子进程会接收到0作为返回值

使用 os.getpid() 能够获得当前进程的pid
使用 os.getppid() 能够获取当前进程父进程pid

！！os.fork() 只支持在unix类操作系统上运行 windows上不能执行！！
'''
# os.fork() 只支持在 unix 和 linux 上运行
import os

pid = os.fork()

if pid == 0:
    print("我是子进程%s,我的父进程是%s"%(os.getpid,os.getppid  ) )
else:
    print("我是父进程%s,我创建了子进程%s"%( os.getpid,pid ))

'''
当执行os.fork()时候，主进程会创建一个子进程
子进程会复制一份和主进程一样的代码、变量、资源，在fork() 之后继续执行相同的内容
'''