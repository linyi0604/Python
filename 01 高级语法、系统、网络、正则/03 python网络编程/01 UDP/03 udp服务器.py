import socket
# 1 开启一个socket套接字 互联网通信 udp协议
server = socket.socket( socket.AF_INET , socket.SOCK_DGRAM )

# 2 绑定ip地址和端口号
server.bind( ("",8080) )

while True :
    # 接收客户端传来的消息
    # 传入参数置顶一次接收数据的大小
    data , addr = server.recvfrom( 1024 )
    print(addr ,":" ,data.decode("utf-8"))

    server.sendto(data, addr)
