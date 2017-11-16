#coding:utf8
#需要加载插件greenlet
import greenlet
import time

def A():
    print("A")
    g2.switch()
    time.sleep(0.5)

def B():
    print("B")
    g1.switch()
    time.sleep(0.5)

g1 = greenlet.greenlet(A)
g2 = greenlet.greenlet(B)

g1.switch()