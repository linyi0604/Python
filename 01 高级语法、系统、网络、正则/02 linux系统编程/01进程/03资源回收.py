'''
 僵尸进程 和 孤儿进程
 僵尸进程: 子进程先死掉，父进程还没死掉的父进程
 
 孤儿进程：父进程死了，子进程还没死掉的子进程
 
 在操作系统中，子进程死掉后，内存等资源都由父进程进行管理回收和释放

 所以 创建出来的子进程我们要自己进行管理，把他们收集
 父进程用os.wait() 可以进行资源回收，会返回两个值 进程的pid 和 一个整数0代表成功 负数代表失败

'''
import os

pid = os.fork()
#子进程会进入这个分支
if pid == 0 :
    print("我是子进程%s，我的父进程是%s"%( os.getpid(),os.getppid() ))
#父进程会进入这个分支
else :
    print("我是父进程%s,我创建了子进程%s"%( os.getpid(),pid ))
    print("我要收集子进程资源：")
    son_pid , result = os.wait()
    print(son_pid , result )

