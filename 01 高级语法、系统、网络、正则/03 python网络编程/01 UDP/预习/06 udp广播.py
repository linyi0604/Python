import socket
# 创建一个udp套接字
s = socket.socket( socket.AF_INET ,socket.SOCK_DGRAM )
# 告诉系统 套接字用来广播
s.setsockopt( socket.SOL_SOCKET , socket.SO_BROADCAST ,1 )
data = input("请输入要广播的内容：")
while data:
    # 注意对广播对象地址的设置
    # broadcast表示广播地址
    s.sendto( data.encode("utf-8"),( "<broadcast>", 8080 ) )
    data = input("请输入要广播的内容:")

s.close()