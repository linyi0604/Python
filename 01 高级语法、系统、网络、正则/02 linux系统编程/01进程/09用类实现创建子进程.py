'''
我们可以定义一个类，继承Process
实例化一个对象的时候，就会创建一个子进程

'''
from multiprocessing import Process
# 自己写一个类 继承在Process
class Proc( Process ):
    #实际上在调用子进程的start() 的时候，默认会执行run() 方法
    #  所以要把主要的逻辑写在run方法当中
    def run(self):
        self.sing()

    def sing(self):
        print("正在唱歌！。。。")


if __name__ == "__main__":
    p = Proc()
    print("子进程开始执行：")
    p.start()
    p.join()