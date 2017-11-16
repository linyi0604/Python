'''

功能： 根据请求不同 返回不同页面或404

1 创建用以监听请求的套接字
2 从已就绪队列中获取到一个客户端套接字 用以和客户端通信使用
3 使用cpython解释器产生的线程会存在GIL全局解释器锁

6.0 版本 实现简单动态

'''

import socket
#from multiprocessing import Process
from threading import Thread
import re
import sys


class HTTPServer(object):
    '''处理http相关请求和响应'''
    def __init__(self ,app ):
        # 开启套接字
        self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.app=app
        self.response_line_header = ""
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
            thread = Thread( target=self.request_handler , args=(client_socket,client_address) )
            thread.start()
    def start_response(self ,status , header_list ):
        '''根据参数 拼接响应头和响应行数据'''
        response_line = "HTTP/1.1%s \r\n"%status
        self.response_line_header += response_line
        for header_name , header_value in header_list:
            self.response_line_header += "%s: %s\r\n"%(header_list , header_value )
    def request_handler(self,client_socket , client_address):
        request_data = client_socket.recv(4096)
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


        #存储环境变量的字典
        env = {
            "file_name":file_name
        }
                        #app是外部引入的模块    env是一个全局资源的字典  start_response是 函数 功能是 拼接相应行和响应头
        response_body = self.app( env ,self.start_response )
        response_data = (self.response_line_header + "\r\n").encode() + response_body

        client_socket.send(response_data)
        client_socket.close()



def main():
    '''
    if len(sys.argv) == 1 :
        print("参数错误！ 用法python3 webxxx.jpy application:app")
        exit()
    module_app = sys.argv[1]

    module_name_app_name = module_app.split(":")
    #可以检测一下是否 module_app_name 长度是否是2
    module_name = module_name_app_name[0]
    app_name= module_name_app_name[1]

    module = __import__(module_name)
    #app_name = module.app
    app = getattr(module , app_name)
    '''

    module = __import__("MyFramework")
    app = module.app
    http_server = HTTPServer( app )
    http_server.bind_and_listen(8080)
    http_server.start()







if __name__ == "__main__":
    main()