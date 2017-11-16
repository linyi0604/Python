import socket
# 1 开一个套接字
server = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

# 2 绑定地址和端口
#ip地址不传入 表示任何一个ip地址都可以
server.bind( ( "",8080 ) )

# 网址字典
dict = {
    "www.baidu.com":"192.168.1.1" ,
    "www.itcast.cn":"192.168.1.1"
}

while True:
    # 3 接收传入的数据和发来消息的地址
    data , addr = server.recvfrom(1024)
    data = data.decode("utf-8")
    print(addr,":",data)
    data = dict.get(data,"404 not found")
    # 4 消息传回
    server.sendto(data.encode("utf-8"), addr)

