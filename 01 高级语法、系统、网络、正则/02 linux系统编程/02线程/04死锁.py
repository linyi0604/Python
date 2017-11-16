'''
死锁 多个变量正想获取资源 都拿不到对方的锁。。发生了死锁，
    解决死锁问题需要一方让步
'''
import multiprocessing
import os
import time

'''
t1 拿着mutex1不放  t2 拿着mutex2不放 
t1阻塞等待mutex2   t2阻塞等待mutex1  发生了死锁
'''
# class MyThread1(multiprocessing.Process):
#     def run(self):
#         print("子进程%s,正在尝试获取锁1"%os.getpid())
#         mutex1.acquire(True)
#         print("子进程%s，获取锁1成功"%os.getpid())
#         time.sleep(1)
#         print("子进程%s,正在尝试获取锁2" %os.getpid())
#         mutex2.acquire(True)
#         print("子进程%s，获取锁2成功"%os.getpid())
#         time.sleep(3)
#         mutex2.release()
#         mutex1.release()
'''解决这个问题我们让t1做出让步'''
class MyThread1(multiprocessing.Process):
    def run(self):
        print("子进程1,正在尝试获取锁1")
        mutex1.acquire(True)
        print("子进程1，获取锁1成功")
        while True:
            print("子进程1,正在尝试获取锁2" )
            flag = mutex2.acquire(False)
            if flag == False :
                mutex1.release()
                mutex1.acquire()
            else :
                print("子进程1，获取锁2成功")
                time.sleep(0.5)
                mutex2.release()
                mutex1.release()
                break



class MyThread2(multiprocessing.Process):
    def run(self):
        print("子进程%s,正在尝试获取锁2"%os.getpid())
        mutex2.acquire(True)
        print("子进程%s，获取锁1成功"%os.getpid())
        time.sleep(1)
        print("子进程%s,正在尝试获取锁1" %os.getpid())
        mutex1.acquire(True)
        print("子进程%s，获取锁1成功"%os.getpid())
        time.sleep(1)
        mutex1.release()
        mutex2.release()


mutex1 = multiprocessing.Lock()
mutex2 = multiprocessing.Lock()
if __name__ == "__main__":

    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()



