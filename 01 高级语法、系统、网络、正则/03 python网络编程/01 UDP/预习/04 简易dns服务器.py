import socket

# 1 启动一个socket  internet通信 udp协议
server_socket = socket.socket( socket.AF_INET , socket.SOCK_DGRAM )

# 2 绑定ip和端口号  不指定ip代表所有程序
server_addr = ("", 8053)
server_socket.bind( server_addr )

# 一个用来存放域名和ip对应的字典
domain_ip={
    "www.itcast.cn" : "192.168.1.2",
    "www.itheima.com":"129.168.1.3",
    "www.google.com":"192.168.1.4"
}

while True:
    # 3 接收客户端发来的消息和ip地址    参数指定接收消息大小
    receive_data , client_addr = server_socket.recvfrom(1024)
    # 串来的为bytes数据 转换成字符串
    domain = receive_data.decode("utf-8")
    print( client_addr ,":" , domain)
    #从字典中查找并返回给客户端
    ip = domain_ip.get(domain , "i don't know")

    server_socket.sendto( ip.encode("utf-8") , client_addr )