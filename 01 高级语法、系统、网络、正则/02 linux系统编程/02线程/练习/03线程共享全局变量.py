'''
多个线程是共享全局变量的
所以可以在函数当中 声明global使用全局变量 
    或者把可变类型数据当作参数传到函数当中，多个线程可以共用
    
但是全局变量大家一块修改就会发生多个线程中数据不能同步的情况
所以引入互斥锁的使用
    mutex = threading.Lock()
    mutex.acquire(True) 以阻塞的方式对全局变量上锁，如果被占用就一直等，成功后会返回Ture
    mutex.acquire(False) 非阻塞方式上锁，成功返回True 失败返回False 并且不等，继续向下执行
    mutex.release() 对全局变量进行解锁
'''
# import threading
# def work():
#     print("我是子进程，我要修改全局变量")
#     global num
#     for i in range(10000000):
#         num +=1
#     print("修改结束")
#
#
# if __name__ == "__main__":
#     num = 0
#     t1 = threading.Thread( target=work )
#     t2 = threading.Thread( target=work )
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print(num)
'''
实际上结果加完了应该是2000000
但是每次结果都不太一样。
多个线程之间获取公共数据进行修改的时候会发生不能同步的情况
这时候引入互斥锁的概念
'''
import threading
def work():
    print("我是子进程，我要修改全局变量")
    global num
    for i in range(1000000):
        flag = mutex.acquire(True)  #以阻塞的方式上锁
       #flag = mutex.acquire(False)  #以非阻塞的方式上锁，如果失败返回False继续向下，时间效率大大降低

        if flag:
            num +=1
            mutex.release()
    print("修改结束")


if __name__ == "__main__":
    mutex = threading.Lock()
    num = 0
    t1 = threading.Thread( target=work )
    t2 = threading.Thread( target=work )
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(num)