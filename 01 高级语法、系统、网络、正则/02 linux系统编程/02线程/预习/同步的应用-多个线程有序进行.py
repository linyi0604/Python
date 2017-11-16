'''
同步的应用：
    通过调整锁，可以让多个进程有序的进行
'''
import threading
import time
class MyThread1(threading.Thread):
    def __init__(self , num):
        threading.Thread.__init__(self )
        self.num = num
    def run(self):
        for i in range(10):
            time.sleep(1)
            if mutex1.acquire(True):
                print("这里是线程%s"%self.num)
                mutex2.release()


class MyThread2(threading.Thread):
    def __init__(self , num):
        threading.Thread.__init__(self )
        self.num = num
    def run(self):
        for i in range(10):
            time.sleep(1)
            if mutex2.acquire(True):
                print("这里是线程%s"%self.num)
                mutex3.release()


class MyThread3(threading.Thread):
    def __init__(self , num):
        threading.Thread.__init__(self )
        self.num = num
    def run(self):
        for i in range(10):
            time.sleep(1)
            if mutex3.acquire(True):
                print("这里是线程%s"%self.num)
                mutex1.release()


if __name__ == "__main__":
    mutex1 = threading.Lock()
    mutex2 = threading.Lock()
    mutex3 = threading.Lock()
    mutex2.acquire()
    mutex3.acquire()

    t1 = MyThread1(1)
    t2 = MyThread2(2)
    t3 = MyThread3(3)

    t1.start()
    t2.start()
    t3.start()