'''
伪装浏览器 发送报文 接收responce
'''
import socket

def main():
    server_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    server_socket.setsockopt( socket.SOL_SOCKET , socket.SO_REUSEADDR ,1 )
    server_address = ( "127.0.0.1",8080 )
    server_socket.connect( server_address )

    request_line = "GET /test1.html HTTP/1.1\r\n"
    request_header = "Host: 127.0.0.1"
    request = request_line + request_header + "\r\n"
    server_socket.send(  request.encode() )

    response = server_socket.recv(4096)
    print(response)

if __name__ == "__main__":
    main()