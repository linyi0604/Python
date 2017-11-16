#encoding:utf8
'''
单线程tcp服务器 同事只能处理一个客户端的请求

'''

import socket
# 开启一个socket
server = socket.socket(socket.AF_INET , socket.SOCK_STREAM )
#设置地址重用
server.setsockopt( socket.SOL_SOCKET , socket.SO_REUSEADDR , 1 )

#绑定地址和ip
server.bind( ("" , 8888 ) )
#开启监听状态
server.listen(128)
while True :
    client , addr = server.accept()
    while True :
        if not data:
            client.close()
            break
        data = client.recv(1024)
        print(addr,":",data.decode())

        client.send(data)


