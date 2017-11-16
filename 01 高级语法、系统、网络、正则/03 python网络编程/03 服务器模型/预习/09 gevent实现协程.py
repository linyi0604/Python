# coding:utf8

#使用python2

import gevent
# #3个greenlet依次运行
# def f(n):
#     for i in range(n):
#         print(gevent.getcurrent(),i)
#
# g1= gevent.spawn(f,5)
# g2 = gevent.spawn(f,5)
# g3 = gevent.spawn(f ,5)
#
# g1.join()
# g2.join()
# g3.join()


#
# # 3个greenlet交替运行
# import gevent
# def f(n):
#     for i in range(n) :
#         print( gevent.getcurrent() , i )
#         #模拟一段操作 不是time下的sleep
#         gevent.sleep(1)
#
# g1 = gevent.spawn(f , 5)
# g2 = gevent.spawn(f , 5)
# g3 = gevent.spawn(f , 5)
#
# g1.join()
# g2.join()
# g3.join()

'''
genvent 并发下载器
实际代码里 我们不会用gevent.sleep() 去切换线程 而是在执行操作io时候，gevent自动切换
'''
from gevent import monkey
import gevent
import urllib2

#有io才做时需要这一句
monkey.patch_all()

def myDownload(url):
    print("得到url:",url)
    response = urllib2.urlopen(url)
    data = response.read()
    print( "%d bytes received from %s"%( len(data) , url ) )

gevent.joinall(
    [
        gevent.spawn( myDownload , "http://www.baidu.com" ),
        gevent.spawn( myDownload , "http://www.itcast.cn" ),
        gevent.spawn( myDownload , "http://www.itheima.com" ),
    ]
)
