'''
udp客户端
'''
import socket

# 1 创建套接字   internet通信 udp协议
client_socket = socket.socket( socket.AF_INET , socket.SOCK_DGRAM )

# 2 服务器地址
server_addr = ( "127.0.0.1" , 8080 )
data = input("请输入要发送的内容：")
# 只要用户输入的内容不为空 就向服务器发送数据
while data:
    # 3 使用sendto方法向服务器发送数据
    # sendto(bytes类型数据， 对方地址 )
    client_socket.sendto( data.encode("utf-8"), server_addr )
    data = input("请输入要发送的内容：")
# 当用户输入数据空时 关闭客户端套接字
client_socket.close()