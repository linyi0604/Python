'''
UDP 用户数据报协议 无连接 简单 面向数据报的运输层协议
    不提供可靠性，只是把应用程序传给ip层的数据报飞洒送出去，但并不能保证他们到达目的地
    不需要建立链接，没有超时重发，传输速率很快
    
UDP特点：udp是面向无连接的通讯协议，udp数据包包括目的端口号和源端口号信息，由于通讯不需要建立连接，所以可以实现广播发送。
    UDP传输数据时有大小限制，必须在64KB之内。
    UDP是一个不可靠的协议发送方锁发送的数据报并不一定以相同的次序达到接收方

UDP适用情况：UDP是面向消息的协议，通信时不需要简历连金，数据的传输自然是不可靠的，UDP一般用于多点通通信和时时业务
    比如：语音广播 视频 qq
        tftp 简单文件传输
        snmp 简单网络管理
        rip 路由信息协议
        dns 域名解释     
'''
'''
socket: 操作系统留给编程人员的接口，实现网络通信
获得一个套接字对象：
socket.socket( AF, type ):
    AF:表示链接类型 AF_INET： 互联网通信
                    AF_UNIX： 本机通信
    typ表示类型：   SOCK_DGRAM 数据包服务 udp协议
                    SOCK_STREAM 流式  tcp协
'''
'''
udp服务器：
'''
import socket
# 1 获取一个套接字 互联网通信 udp协议
socket = socket.socket( socket.AF_INET , socket.SOCK_DGRAM )
# 2 为服务器绑定ip和端口
# ip空代表任何ip都可以访问我的服务器 端口号需要指定，在动态地址空间
address = ( "", 8080 )
socket.bind(address)
while True:
    # 3 阻塞等待客户端传来的消息
    # recvfrom() 参数指定一次接收多大数据，返回二元组 数据 和 对面地址
    data , addr = socket.recvfrom(1024)
    if not data :
        break

    print(addr , ":" , data.decode("utf-8"))

    # 4 利用sendto 可以发送消息 传入 数据和 地址
    socket.sendto( data , addr )
socket.close()












