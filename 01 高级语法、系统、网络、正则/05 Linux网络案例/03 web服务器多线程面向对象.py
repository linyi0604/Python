'''

功能： 根据请求不同 返回不同页面或404

1 创建用以监听请求的套接字
2 从已就绪队列中获取到一个客户端套接字 用以和客户端通信使用
3 使用cpython解释器产生的线程会存在GIL全局解释器锁

实现用面向对象的方式 代码重构

'''

import socket
#from multiprocessing import Process
from threading import Thread
import re










class HTTPServer(object):
    '''处理http相关请求和响应'''
    HTML_ROOT_PATH = "."

    def __init__(self ):
        # 开启套接字
        self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    def bind_and_listen(self , port=8080):
        # 绑定端口 关联进程服务和端口
        server_address = ("", port )
        self.listen_socket.bind(server_address)
        # 开启监听
        self.listen_socket.listen(128)
    def start(self):
        while True:
        # 取出客户端套接字
            client_socket , client_address = self.listen_socket.accept()
            print("accept from %s connected"%str(client_address))

            #创建一个进程为客户端服务
            #process = Process( target=request_handler , args=(client_socket,client_address) )
            #process.start()

            thread = Thread( target=self.request_handler , args=(client_socket,client_address) )
            thread.start()
            #client_socket 交给子进程会复制一份一样的 在父进程没有用了
            #client_socket.close()
    def request_handler(self,client_socket , client_address):
        request_data = client_socket.recv(4096)
        #print(request_data)
        #将request_data 转换字符串
        request_string_data = request_data.decode()

        #切割请求报文 \r\n
        lines_list = request_string_data.split( "\r\n" )
        #拿到请求行 "GET /index.html HTTP/1.1"
        request_line = lines_list[0]
        res = re.match( r"\w+\s+(/[^ ]*) +",request_line )
        if not res :
            return
        #获取到请求的资源地址名称 转换成相对路径
        file_name = res.group(1)
        if file_name == "/":
            file_name = "/index.html"
        try:
            file_data = open( self.HTML_ROOT_PATH+file_name , "rb" )

        except FileNotFoundError as e:
            response_line = "HTTP/1.1 404 Not Found\r\n"
            response_header = "Server: HTTPServerByPython2.0\r\n"
            response_body = "%s"%str(e)
            response_data = (response_line + response_header + "\r\n" + response_body).encode()
        else:
            response_line = "HTTP/1.1 200 OK\r\n"
            response_header = "Server: HTTPServerByPython2.0\r\n"
            response_body = file_data.read()
            response_data = (response_line + response_header + "\r\n").encode() + response_body
            file_data.close()



        client_socket.send(response_data)
        client_socket.close()



def main():

    http_server = HTTPServer()
    http_server.bind_and_listen(8080)
    http_server.start()







if __name__ == "__main__":
    main()