import socket
# 创建TCP协议对应为SOCK_STREAM 流式
server_sock = socket.socket( socket.AF_INET , socket.SOCK_STREAM )

# 绑定ip和端口
address = ( "",8080 )
server_sock.bind(address)

#让服务器的sock开启坚挺 等待客户端的连接请求
#listen中的参数表示已建立链接和半链接的总数
# 如果当前已经建立链接数和半链接数已经达到设定值，那么新客户端不会被立即connect，会等客户端
server_sock.listen(128)

#使用accept方法接收客户端的链接请求
#如果有新的客户端来链接服务器 那么及iuchanshengyige新的套接字专门为这个客户端服务
#client_sock用来为这个客户端服务 与客户端形成一对一连接
#server_sock就可以生下来专门等待其他新客户端的链接请求
#client_addr是请求链接的客户端的地址信息，为元组，包含用户的ip和端口号
client_sock,client_addr = server_sock.accept()
print("客户端%s：%s进行了链接" %client_addr )
#recv() 方法可以接收客户端发送过来的数据，指明最大收取的字节数
recv_data = client_sock.recv( 1024 )
#python3 中收到的数据为bytes类型#revc_data.decode() 将bytes转为str类型
print("接收到的数据为：",recv_data.decode("utf-8"))

#send() 方法向客户端发送数据 要求发送bytes类型数据
client_sock.send( "thank you!\n".encode("utf-8") )

#关闭与客户端链接的socket
#只要挂壁了 就意味着不再为这个客户端服务 只能再次链接
client_sock.close()

#关闭服务端的监听socket
#关闭套接字 不接收任何链接
server_sock.close()

