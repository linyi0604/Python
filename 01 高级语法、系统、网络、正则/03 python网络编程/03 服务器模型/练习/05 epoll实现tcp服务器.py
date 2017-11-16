#coding=utf-8
'''
socket.epoll( socket.fileno() , socket.EPOLLIN|socket.EPOLLET )
获取一个epoll对象之后 给socket进行绑定事件  in代表输入   et代表一种以触发  lt表示如果不处理下次就不触发

epoll 会检查活跃的 文件编号 并把他放在poll() 返回列表里面
它只服务活跃的内容 所以很节省时间


'''

import socket
import select
import queue
#开启一个服务器的套接字
server = socket.socket( socket.AF_INET,socket.SOCK_STREAM )
#设置地址重用
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR , 1)
#绑定地址和端口
server.bind(("",8888))
#开启监听模式
server.listen(128)

#创建一个epoll对象
epoll = select.epoll()
# 为server注册 绑定监听
epoll.register( server.fileno(), select.EPOLLIN | select.EPOLLET )

#用于存储socket的全局字典 key： fileno  value：socket
socket = {}
socket[server.fileno()] = server
#存储地址的字典  key； fileno valuie: addr
addrs = {}
#存发来数据的字典 key: fileno value: queue
message = {}
while True:
    #event_list 里面元组的列表   元素是( fd ,event )  fd是文件修饰符    event是触发的事件类型
    event_list = epoll.poll()
    for fd , event in event_list:
        # 如果是服务器 说明有客户端来连接了
        if fd == server.fileno():
            #接受客户端的连接
            client , addr = socket[server.fileno()].accept()
            print( addr , "连接！" )
            socket[client.fileno()] = client
            addrs[client.fileno()] = addr
            message[client.fileno()] = queue.Queue()
            #为连接来的客户端绑定监听
            epoll.register( client.fileno() , select.EPOLLIN | select.EPOLLET )
        #如果是发来消息的
        elif event == select.EPOLLIN :
            data = socket[fd].recv(1024)
            #如果客户端下线了
            if not data:
                print(addrs[fd],"下线！")
                del addrs[fd]
                #为客户端解除监听的绑定
                epoll.unregister( fd )
                del message[fd]
                socket[fd].close()
                del socket[fd]
            #发来了数据
            else :
                print( addrs[fd],":",data.decode() )
                #发来的消息放进消息队列
                message[fd].put(data)
                #更改该客户端绑定的事件 改为检查等待服务器回复消息
                epoll.modify( fd , select.EPOLLOUT | select.EPOLLET )
        # 如果是等待服务器回复消息的
        elif event == select.EPOLLOUT :
            if message[fd].empty():
                pass
            else :
                msg = message[fd].get()
                socket[fd].send(msg)
                #更改绑定类型改为检测发来消息
                epoll.modify( fd, select.EPOLLIN | select.EPOLLET )
        else :
            pass



