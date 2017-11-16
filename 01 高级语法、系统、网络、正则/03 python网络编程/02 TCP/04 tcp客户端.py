import socket
# 1 开启一个套接字
client = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
# 链接指定服务器
address = ( "127.0.0.1", 8080 )
client.connect( address )

while True :
    data = input("发送：")
    client.send( data.encode("utf-8") )
    if not data :
        break
    data = client.recv( 1024 )
    print(data.decode())

