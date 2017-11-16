#coding:utf8
'''
epoll的优点：
     1 没有最大并发量的链接限制，能打开的fd的上线远远大于1024
     2 效率提升 不是轮训的方式 不会随着fd的数目的增大而效率下降。只有年活跃的可用的FD才会调用callback函数
'''

import socket
import select

# 创建套接字
server = socket.socket( socket.AF_INET , socket.SOCK_STREAM )

# 设置可重用绑定信息
server.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR , 1 )

# 绑定服务器信息
server.bind( ("", 8080) )
# 开启监听状态
server.listen(10)

# 创建一个epoll对象
epoll = select.epoll()

#测试 用来打印套接字对应的文件描述符
#print(server.fileno())
#print(select.EPOLLIN | EPOLLET )

#注册事件到epoll中
#epoll.register(fd [,eventmask] )
# 注意 如果fd已经注册过则会抛出异常
# 将创建的套接字添加到epoll的事件监听中
epoll.register(server.fileno() , select.EPOLLIN|select.EPOLLET )

connections = {}
addresses = {}

# 循环等待客户端的到来或者访问对方发送的数据
while True:
    # epoll 进行扫描的地方 为指定时间则为阻塞等待
    epoll_list = epoll.poll()
    #对事件进行判断
    for fd , events in epoll_list:
        # print(fd)
        # print(event)\

        #如果是socket创建的套接字 就被激活
        if fd == server.fileno() :
            conn, addr = server.accept()
            print(addr , "已连接！")
            #将 conn 和addr保存起来
            connections[conn.fileno()] = conn
            addresses[conn.fileno()]= addr

            #向epoll中注册链接socket的可读事件
            epoll.register( conn.fileno() , select.EPOLLIN | select.EPOLLET)

        elif events == select.EPOLLIN:
            #从激活fd上接收
            recvData = connections[fd].recv(1024)

            if len(recvData)> 0 :
                print(recvData)
            else :
                # 从epoll 中移除该链接fd
                epoll.unregister(fd)
                #server侧主动关闭该链接
                connections[fd].close()

                print(addresses[fd],"已下线")



