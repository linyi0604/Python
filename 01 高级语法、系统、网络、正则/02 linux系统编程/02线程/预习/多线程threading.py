'''
线程在python的thread模块，很底层，python为我们封装了threading模块来使用多线程

'''
#多线程实现执行一段程序
import threading
import time
import random

# def work():
#     print("亲爱滴~我可以吃饭吗~？")
#     time.sleep(random.random())
#
# if __name__ == "__main__":
#     for i in range(5):
#         p = threading.Thread( target = work )
#         p.start()


'''
主线程会等待所有子线程全部结束之后才结束
'''
# def sing():
#     print("正在唱歌！")
#
# if __name__ == "__main__":
#     print("开始！")
#     p = threading.Thread( target = sing )
#     p2 = threading.Thread( target = sing )
#     p.start()
#     p2.start()
#
#     #time.sleep(3)
#     print("结束！")

'''
查看线程的数量
'''

def sing():
    for i in range(3):
        print("正在唱歌！！")
        time.sleep(2)
def dance() :
    for i in range(3):
        print("正在跳舞!!")
        time.sleep(4)


if __name__ == "__main__":
    print("开始执行主程序：")
    ts = threading.Thread( target=sing )
    td = threading.Thread( target=dance )

    ts.start()
    td.start()

    while True :
        length = len( threading.enumerate() )
        print("当前执行的进程数目是%s"%length)

        if length == 1:
            break

        time.sleep(0.5)

