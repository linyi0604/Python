'''
线程与进程：
    线程是计算机cpu调度的最小单位，进程是资源分配的最小单位
    进程互相不共享数据 进程之间相互独立
    多个线程共享主线程的一份数据
    进程调度消耗空间大，线程调度快捷
    线程调度因为共享数据而不安全，进程之间没有共享数据很安全
'''
'''
使用threading模块进行创建进程，与Process 使用方法类似
主线程会等待子线程结束之后才会在结束

'''
'''
current_thread() 还获得当前的线程
enumerate() 返回当前所有线程
'''
import threading
# 定义一个工作函数 需要线程帮助我们完成
def sorry(num):
    print("%s 对不起我错了  我是线程%s"%( num, threading.current_thread().name ))


if __name__=="__main__":
    for i in range(10):
        #Thread() 帮助我们开启线程
        #参数target绑定的工作函数 args传入target的参数 name是线程名字 可以不传入
        t = threading.Thread( target=sorry , args=(i,),name="啊哈哈%s"%i )
        t.start() #开启线程

    #enumerate() 返回当前所有线程的元组
    for i in threading.enumerate() :
        if i is not threading.current_thread():
            i.join() #阻塞停掉线程后 主进程回收资源

    print("结束")