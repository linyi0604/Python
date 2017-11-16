'''
UDP 用户数据报协议
    是一个无连接的简单的面向数据报的运输层协议。

'''

'''
创建socket
    socket( AddressFamily , Type )
        AddressFamily： AF_INE 用于internet进程之间通信
                        AF_UNIX用于同一台机器进程间通信
        Type: SOCK_STREAM 流式套接字，主要用于TCP协议
              SOCK_DGRAM  数据报套接字 主要用于UDP协议
'''
#创建一个tcp套接字
import socket
# s = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
#创建一个 udp socket
# s = socket.socket( socket.AF_INET , socket.SOCK_DGRAM )















