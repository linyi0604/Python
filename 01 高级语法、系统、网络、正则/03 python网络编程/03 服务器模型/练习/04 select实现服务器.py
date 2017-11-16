
#coding=utf-8
'''
select 是一个封装的工具，他能帮助我们管理参数列表里面元素的变化
read_list , write_list , erro_list = select(input_list , output_list , erro_list)
传入三个参数：
    input_list: 连接到服务器的客户端socket的元组，select帮我们检测 ，把里面对服务器发送消息的socket放进返回值read_list里面
    output_list:连接到服务器的客户端socket元组，select帮我们检测等待我们传送消息过去并且网络畅通的socket会放进write_list中
    erro_list : 一般不会用到
返回值：
    read_list : 传来消息的socket会放进里面
    write_list：等待我们回复消息的并且网络畅通的socket会放进里面
    erro_list:  一般用不到


select会采用轮询的方法，检测每一个列表元素是否满足要求
    所以效率很低
'''


import socket
import select
import queue
#开启一个服务器套接字
server = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
#设置地址重用
server.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR ,1 )
#绑定地址和端口
server.bind(("",8888))

#开启监听
server.listen( 128 )

#存储连接到服务器的客户端
input_list = [server ]
#存储等待回复消息的客户端
output_list =[]

#存储客户端socket的地址字典
addrs = {}
#存储客户端发来消息的字典
message = {}

while True:
    #开启select帮助管理
    read_list, write_list , erro_list = select.select( input_list , output_list ,[] )
    #对发来消息的客户端进行处理
    for socket in read_list:
        #如果活跃的是 服务器，说明有客户端来连接，我们要接收连接
        if socket == server :
            client , addr = socket.accept()
            print( addr,"连接！" )
            addrs[client] = addr
            #放到发来消息的列表当中管理监控
            input_list.append( client )
            #为这个客户端开一个消息队列
            message[client]=queue.Queue()
        #其他情况，是客户端来消息了
        else :
            data = socket.recv(1024)
            #如果客户端下线了
            if not data:
                print(addrs[socket],"下线！")
                output_list.remove(socket)
                input_list.remove(socket)
                del addrs[socket]
                del message[socket]
                socket.close()

            print(addrs[socket],":",data.decode())
            #把客户端来的消息放消息队列
            message[socket].put(data)
            #把客户端socket放到等待回复的列表当中监控
            output_list.append(socket)
    #对等待回复的客户端进行回复
    for socket in write_list:
        if message[socket].empty() :
            pass
        else:
            socket.send( message[socket].get() )















