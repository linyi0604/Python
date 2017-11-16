import socket
# 开启一个socket  internet传输  udp协议
client_socket = socket.socket( socket.AF_INET , socket.SOCK_DGRAM )
server_addr = ("127.0.0.1" , 8053)
domain = input("请输入要查询的域名：")
while domain :
    #向服务器发送要查询的域名
    client_socket.sendto( domain.encode("utf-8") , server_addr )
    #接收服务器发过来的ip信息
    ip = client_socket.recv(1024)
    print(ip.decode("utf-8"))
    domain = input("请输入要查询的域名:")

client_socket.close()