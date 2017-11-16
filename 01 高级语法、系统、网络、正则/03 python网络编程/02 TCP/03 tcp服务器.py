import socket

# 1 开启一个socket 套接字
server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

# 设置地址重用 防止无限回荡 无法关闭四次挥手
server.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)

# 2 绑定ip和端口号
server.bind( ( "", 8080 )  )

# 3 开启监听 监听客户端的三次握手,指定可以接收的最大链接数
server.listen(128)

while True:
    # 4 接收客户端的套接字
    client_socket, client_address = server.accept()
    print(client_address,"链接成功！")
    while True:
        data = client_socket.recv(1024)
        if not data :
            print(client_address,"已经下线！")
            break
        print(data.decode())
        response = input("回复：")
        client_socket.send( response.encode("utf-8") )
    client_socket.close()


