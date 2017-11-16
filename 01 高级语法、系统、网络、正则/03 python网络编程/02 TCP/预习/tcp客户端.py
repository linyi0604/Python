import socket
#创建客户端socket 跟服务器进行通讯
#tcp协议应对sock_stream
client_sock = socket.socket( socket.AF_INET , socket.SOCK_STREAM )

#connect方法链接服务器
server_addr = ( "127.0.0.1",8080 )
client_sock.connect( server_addr )

#提示用户输入发送的数据
msg = input("请输入要发送的内容:")
#send（）方法发送数据
client_sock.send( msg.encode() )

#recv() 收对方发来的数据 设置最大字节数
# 在tcp中 如果传来数据超过最大字节数，会调用多次读取回来 不会丢数据
recv_data = client_sock.recv( 1024 )
print("收到服务器返回消息：%s"%recv_data.decode())

#关闭客户端
client_sock.close()