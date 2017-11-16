import socket

# 1 开启一个套接字 运用互联网之间的通信 udp协议
client = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

# 2 地址和端口号
address = ("127.0.0.1" , 8080 )

data = input( "请输入要发送的内容：" )

while data:
    # 3 向客户端发送消息
    # sandto() 需要发送bytes类型的数据
    # str.encode()  字符串转换成bytes类型
    client.sendto( data.encode("utf-8"), address )

    # 4 接收服务器发送过来的消息
    # bytes类型转换成字符串类型
    rcv = client.recv( 1024).decode("utf-8")
    print(rcv )

    data = input("请输入要发送的内容：")