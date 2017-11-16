'''
功能： 实现一个web服务器，多线程的方式
    根据请求返回不同的页面或者404
'''
import socket
from threading import Thread
import re
#一个子线程的子类 帮助我们解析请求头 和发送响应
class Response(Thread):
    def __init__(self , socket , address ):
        Thread.__init__(self)
        self.socket = socket
        self.address = address
    def run(self):
        #接收请求 转换成字符串
        request = self.socket.recv(4096).decode()
        #获取请求的路径
        request_line = request.split("\r\n")[0]
        res = re.search( r"\w+\s+(/[^ ]*)\s+", request_line )
        if not res:
            return
        file_name = "." + res.group(1)
        if file_name == "./" :
            file_name = "./index.html"

        #打开请求的路径
        try:
            # 文本文件可以以二进制形式打开，打开read的结果就是bytes类型
            file = open(file_name , "br")
        #如果没有这个文件会打开失败
        except FileNotFoundError as e :
            #构造返回的response报文
            response_line = "HTTP/1.1 404 Not Found\r\n"
            response_header = "Server:PythonProgram2.0\r\n"
            response_body = str(e)
            response = (response_line + response_header + "\r\n" + response_body).encode()
        else:
            # 构造返回的response报文
            response_line = "HTTP/1.1 200 OK\r\n"
            response_header = "Server:PythonProgram2.0\r\n"
            response_body = file.read()
            response = (response_line + response_header + "\r\n").encode() + response_body
        self.socket.send( response )
        self.socket.close()




def main():
    #创建套接字
    server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    #设置地址重用
    server_socket.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR , 1)
    #绑定端口
    server_socket.bind( ( "",8080 ) )
    #开启监听 等待客户端连接
    server_socket.listen(128)

    while True:
        # 接收客户端的连接
        client_socket, client_address = server_socket.accept()
        # 客户端 任务丢给线程去做  线程用类对象来实现
        t = Response( client_socket , client_address )
        t.start()





if __name__ == "__main__":
    main()