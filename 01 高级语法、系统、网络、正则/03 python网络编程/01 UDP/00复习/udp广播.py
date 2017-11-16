import socket
server = socket.socket( socket.AF_INET , socket.SOCK_DGRAM )

# 声明这个socket用于广播
#传入三个参数 对这个socket层次设置  设置成广播socket  立即生效
server.setsockopt( socket.SOL_SOCKET,socket.SO_BROADCAST, 1)
data = "这是广播测试".encode("utf-8")
# 传入地址 <broadcast> 代表要广播当前子网的所有ip
server.sendto( data, ( "<broadcast>",8080 ) )
