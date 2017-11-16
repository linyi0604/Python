#coding=utf-8
'''
协程： 程序员自己决定要阻塞的时候执行一下其他部分 结束后会掉
'''

#
# import time
# def A():
#     while True:
#         print("---A---")
#         yield
#         time.sleep(0.5)
#
# def B(c):
#     while True:
#         print("---B---")
#         c.next()
#         time.sleep(0.5)
#
# a = A()
# B(a)

#
#
# '''
# greenlet 实现协程
# '''
# import greenlet
# import time
#
# def test1():
#     while True:
#         print("11111")
#         gr2.switch()
#         time.sleep(0.5)
#
#
# def test2():
#     while True:
#         print("222222")
#         gr1.switch()
#         time.sleep(0.5)
#
#
#
# gr1 = greenlet.greenlet(test1)
# gr2 = greenlet.greenlet(test2)
#
# gr1.switch()


# '''
# gevent实现协程
# '''
# import gevent
# def f(n):
#     for i in range(n):
#         print( gevent.getcurrent() , i )
#         gevent.sleep(0.5)
#
# g1 = gevent.spawn( f , 5 )
# g2 = gevent.spawn( f , 5 )
#
# g1.join()
# g2.join()

#
# '''
# gevent的并发器
# '''
# import gevent
# import urllib2
# #捕获io操作 自动执行协程切换
# gevent.monkey.patch_all()
#
# def down_load(url):
#     print("开始下载:",url)
#     html = urllib2.urlopen(url)
#     txt = html.read()
#     print(url,"总长度",len(txt))
#
#
# gevent.join(
#     {
#         gevent.spawn( down_load , "http://www.baidu.com" ),
#         gevent.spawn( down_load , "http://www.itheima.com" ),
#         gevent.spawn( down_load , "http://www.itcast.cn" )
#     }
#
# )


