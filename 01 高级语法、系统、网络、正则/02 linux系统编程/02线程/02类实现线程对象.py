'''

类进程Thread  实现这个类就是实现一个线程
线程.start() 默认执行run方法 所以要重写run方法

'''
from threading import Thread ,current_thread,enumerate

class ThreadDemo(Thread):
    def run(self):
        print("我是子线程%s"%current_thread().name)

if __name__ == "__main__":
    print("开始")
    for i in range(10):
        p = ThreadDemo()
        p.start()

    for i in enumerate():
        # 不是当前的主进程的时候进行回收
        if i is not current_thread():
            i.join()

    print("结束")