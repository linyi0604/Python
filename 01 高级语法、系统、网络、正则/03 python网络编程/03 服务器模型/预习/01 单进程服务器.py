'''
单进程服务器
'''
import socket
# 开启一个服务器socket
server = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
# 绑定ip和端口
server_address = ( "",8080 )
server.bind(server_address)
# 设置名字重用   对本socket设置，重用名字， 生效
server.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR , 1 )
# 开启监听状态 指定最大连接数量128
server.listen(128)

while True:
    #接收客户端的链接 接收处理客户端的套接字和地址
    client_socket , client_address = server.accept()
    while True:
        # 接收客户传来的消息
        data = client_socket.recv(1024)
        if not data:
            break
        print(data.decode("utf-8"))
        client_socket.send(input("回复：").encode())
    client_socket.close()

server.close()
