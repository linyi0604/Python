'''
功能： 接收请求 返回固定页面

1 创建用以监听请求的套接字
2 从已就绪队列中获取到一个客户端套接字 用以和客户端通信使用
3 
'''

import socket
from multiprocessing import Process

def request_handler(client_socket , client_address):
    request_data = client_socket.recv(4096)
    #print(request_data)
    #响应报文
    #响应行    协议版本  状态码 提示
    response_line = "HTTP/1.1 200 OK\r\n"
    response_header = "Server: HTTPServerByPython1.0\r\n"
    response_body = "hello python!"
    response_data = response_line + response_header +"\r\n" + response_body
    client_socket.send(response_data.encode())


    client_socket.close()



def main():
    # 开启套接字
    listen_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR ,1)
    # 绑定端口 关联进程服务和端口
    server_address = ( "", 8080 )
    listen_socket.bind( server_address )
    #开启监听
    listen_socket.listen( 128 )

    while True:
    # 取出客户端套接字
        client_socket , client_address = listen_socket.accept()
        print("accept from %s connected"%str(client_address))

        #创建一个进程为客户端服务
        process = Process( target=request_handler , args=(client_socket,client_address) )
        process.start()
        #client_socket 交给子进程会复制一份一样的 在父进程没有用了
        client_socket.close()






if __name__ == "__main__":
    main()