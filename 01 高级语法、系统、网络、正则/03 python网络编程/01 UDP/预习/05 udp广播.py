import socket

# 1 开一个套接字
server = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

# 2 设置一下 该套接字用于 广播
#   第一个参数表示对自己进行设置 第二个参数表示广播 第三个参数表示生效
server.setsockopt( socket.SOL_SOCKET , socket.SO_BROADCAST ,1 )

while True:
    data = "正在广播"
    # <broadcast> 在广播当中代替地址
    server.sendto(data.encode() , ("<broadcast>" ,8080 ))
    server.recvfrom( 1024)