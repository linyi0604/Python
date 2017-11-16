#coding=utf-8
'''
单进程tcp服务器设置非阻塞，可以实现多个客户端的连接
利用setblocking
'''
import socket

#开启一个套接字
server = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
#绑定地址
server.bind( ( "", 8888 ) )
#设置地址复用
server.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR ,1)
#设置非阻塞  设置非阻塞后 如果没有客户端连接会报异常
server.setblocking(False)
#开启监听模式
server.listen(128)

while True:
    try:
        #接受客户端的请求
        client , addr = server.accept()
        print(addr,"上线！")
        while True:
            #接受消息
            data = client.recv(1024)
            if not data:
                print(addr,"下线！")
                client.close()
                break

            print(addr,":",data.decode())

            #数据处理并返回
            client.send(data)
    except BlockingIOError:
        pass

