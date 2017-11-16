#coding:utf8
'''
udp 用户数据报协议 是一个面向无连接，简单的 面向数据报的运输协议。
    udp不提供可靠的服务
udp一般用于多点通信和实施的数据业务
    例如 语音广播、视频、 qq 、tftp snmp rip dns
    速度快、不安全
    
    
    
    
socket ： 操作系统为我们封装socket 套接字进行网络通信
    
创建套接字：
    socket.socket( AdressFamily , type )
    AF 的类型有两种：
            socket.AF_INET 互联网通信
            socket.AF_UNIX 本机进程之间的通信
            
    Type有两种： 
        SOCK_STREAM 流套接字 用于TCP协议
        SOCK_DGRAM  数据报套接字 用于udp协议
'''


'''
udp : 无连接 简单 面向数据报的协议
优点： 时时行高 效率高 
缺点： 不可靠 无序
'''
'''
socket： 封装了底层通讯的一套工具
    socket.socket( AF_INET, SOCK_GRAM )
    要想网络通讯 必须创建套接字

服务器端：
    1 创建套接字
    2 绑定ip和端口
    3 阻塞等待客户端数据到来
    4 处理客户端的请求
    5 返回处理的请求结果
客户端：
    1 创建套接字
    2 发送消息
    3 阻塞等待服务器的返回结果
    4 关闭套接字

DNS服务器：
    维护了域名和ip地址

udp广播：
    1 设置socket  setsockopt( SOL_SOCKET , SO_BROADCAST ,1  )
    2 sendto 地址的使用，(<broadcast>  , 8888 )  对方端口
    
     
    
    
    
    
    
    
    
    
    
    

'''