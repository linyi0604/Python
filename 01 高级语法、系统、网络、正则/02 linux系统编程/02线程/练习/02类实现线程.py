'''
自己创建一个类 继承threading.Thread
这样实现对象的时候相当于创建了一个线程

调用start方法的时候实际上调用了内部的run方法所以要重写run方法
    把我们希望线程帮我们做的工作放在run方法里面
'''
import threading
class myThread(threading.Thread):
    def run(self):
        print("我是线程%s"%threading.current_thread().name)


if __name__ == "__main__":
    t = myThread()
    t.start()
    t.join()
