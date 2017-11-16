#coding:utf8

#需要在python2下面执行
'''
协程： 通俗的理解 在一个线程中某个函数 可以在任何地方保存当前函数的一些临时变量信息
    然后切换到另外一个函数中执行，并且切换的次数以及什么时候再切换回来都由开发人员自己决定
'''

import time

def A():
    while True:
        print("A")
        yield
        time.sleep(0.5)
def B(c):
    while True :
        print("B")
        c.next()
        time.sleep(0.5)


if __name__ == "__main__":
    a = A()
    B(a)