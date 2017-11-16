import socket
# 1 开启一个socket 互联网通信 运用tcp协议
server = socket.socket( socket.AF_INET , socket.SOCK_STREAM )

# 2 设置socket重用地址 避免错误
server.setsockopt( socket.SOL_SOCKET , socket.SO_REUSEADDR , 1 )

# 3 为服务器绑定地址
addr = ("", 8080)
server.bind(addr)

#开启监听状态 指定最大链接数 超过会等待
server.listen(128)
# 收到链接请求

client_socket , client_addr = server.accept()
print( "%s, %s 已连接！" %client_addr  )

while True:
    data = client_socket.recv(1024)
    print( client_addr, "发来消息：",data.decode())
    data = input("回复：")
    if len(data)>0 :
        client_socket.send( data.encode() )
    else :
        client_socket.close()
        break

server.close()