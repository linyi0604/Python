#coding=utf-8

import socket

'''
单进程服务器，不能同时处理多个客户端的请求
'''

server = socket.socket( socket.AF_INET , socket.SOCK_STREAM )

#设置地址复用
server.setsockopt( socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)

server.bind( ("", 8888 ) )


server.listen(128)

while True:
    client_sock, addr = server.accept()

    while True:
        data = client_sock.recv(1024)
        if data :
            print(data.decode() )
            client_sock.send(data)
        else :
            client_sock.close()
            break

