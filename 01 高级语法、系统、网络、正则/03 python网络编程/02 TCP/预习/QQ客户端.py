import socket
client = socket.socket( socket.AF_INET , socket.SOCK_STREAM )

addr = ( "127.0.0.1" , 8080 )
client.connect( addr )

while True:
    data = input("请输入：")
    if len(data) > 0 :
        client.send( data.encode() )
        rev_data = client.recv( 1024 )
        print("收到消息：",rev_data.decode())
    else :
        break
client.close()





