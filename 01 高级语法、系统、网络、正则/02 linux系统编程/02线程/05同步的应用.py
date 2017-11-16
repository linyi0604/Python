'''
利用互斥锁，可以实现内部控制功能完成的顺序，不需要调用者在调用的时候进行控制
'''
import threading
import time
def wokr1():
    for i in range(10):
        mutex1.acquire()
        time.sleep(1)
        print("work1")
        mutex2.release()

def wokr2():
    for i in range(10):
        mutex2.acquire()
        time.sleep(1)
        print("work2")
        mutex3.release()

def wokr3():
    for i in range(10):
        mutex3.acquire()
        time.sleep(1)
        print("work3")
        mutex1.release()

mutex1 = threading.Lock()
mutex2 = threading.Lock()
mutex3 = threading.Lock()
mutex2.acquire()
mutex3.acquire()

if __name__ == "__main__":
    t1 = threading.Thread(target=wokr1 )
    t2 = threading.Thread(target=wokr2 )
    t3 = threading.Thread(target=wokr3 )

    t1.start()
    t2.start()
    t3.start()