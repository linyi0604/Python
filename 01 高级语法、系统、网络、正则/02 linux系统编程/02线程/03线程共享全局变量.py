'''
多个线程对象实际上是共享进程当中的资源变量等等
'''
import threading
num = 10
list = [1]


def changeNum():
    global num
    print("我是子进程%s,我在增加num"%threading.current_thread().name)
    num+=1

def changeList(li):
    print("我是子进程%s,我在追加list" % threading.current_thread().name)
    list.append(threading.current_thread().name)

if __name__ == "__main__":
    for i in range(5):
        t1 = threading.Thread( target=changeNum )
        t2 = threading.Thread( target=changeList , args=(list,))
        t1.start()
        t2.start()

    for t in threading.enumerate():
        if t is not threading.current_thread():
            t.join()
    print(num)
    print(list)