'''
由于线程共享进程的变量和资源
当多个进程共同修改全局变量的时候就会发生错误，不能达到多个进程之间数据的同步
例如：
'''

# import threading
# #绑定函数让桉树进行对全局数据的累加
# def add():
#     global num
#     for i in range( 1000000 ):
#         num += 1
#
# if __name__ == "__main__":
#     num = 0
#     t1 = threading.Thread(target=add )
#     t2 = threading.Thread(target=add )
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print(num)

'''
两个线程都对全局变量进行累加操作，由于系统调度 会导致num不能同步 会导致更新出错
这个时候我们引入互斥锁
在调用数据之前开锁，其他线程无法访问
在调用之后解锁，其他线程可以访问全局变量
threading.Lock
'''
import threading
#绑定函数让桉树进行对全局数据的累加
def add():
    global num
    for i in range( 1000000 ):
        #使用数据之前打开互斥锁
        #mutex.require(True)表示阻塞，如果不能上锁就一直等在这里 一直到能上锁为止
        #               如果传入False则上锁不成功还会继续向下进行
        flag = mutex.acquire( True )
        if flag:
            num += 1
            mutex.release()
        #使用之后关闭互斥锁

if __name__ == "__main__":
    #引入互斥锁
    mutex = threading.Lock()

    num = 0
    t1 = threading.Thread(target=add )
    t2 = threading.Thread(target=add )
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(num)