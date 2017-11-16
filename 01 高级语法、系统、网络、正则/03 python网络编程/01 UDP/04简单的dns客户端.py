import socket
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

addr = ("127.0.0.1", 8080)

data = input("请输入网址：")

while data:
    client.sendto( data.encode(),addr )

    data = client.recv(1024)

    print(data.decode())

    data = input("请输入网址：")

