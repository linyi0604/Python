#coding:utf8
import socket
import threading
import re







class HttpServer(object):
    def __init__(self , app):
        self.server_socket = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
        self.server_socket.setsockopt( socket.SOL_SOCKET , socket.SO_REUSEADDR , 1 )
        self.wsgi = app
        self.response_head_line = ""
    def bind_listen(self, port=8080):
        self.server_socket.bind( ( "" , port ) )
        self.server_socket.listen(128)
    def start(self):
        while True:
            client_socket , client_address = self.server_socket.accept()
            thread = threading.Thread( target=self.handle_client , args=( client_socket,client_address ) )
            thread.start()
    def handle_client(self, client_socket , clent_address ):
        request = client_socket.recv(4096).decode()
        #GET /getinfo.py HTTP/1.1
        request_path = re.match( r"\w+\s+(/[^ ]*)\s+", request )
        if not request_path:
            return
        #拿到了请求的路径
        request_path = request_path.group(1)

        #全局资源字典 给wsgi框架去获取全局资源
        environment = {
            "file_name":request_path
        }
        response_body = self.wsgi( environment, self.set_response_line_head )
        response_data = (self.response_head_line + "\r\n" ).encode() + response_body


        client_socket.send( response_data )
        client_socket.close()




    #该函数传给wisgi框架 去帮我们生成响应行和相响应头
    def set_response_line_head(self, status , head_list ):
        self.response_head_line = "HTTP/1.1 %s\r\n" %status
        for head_name , head_value in head_list:
            self.response_head_line += "%s: %s\r\n"%( head_name , head_value )



def main():

    module = __import__("myFramework")
    app = module.app


    httpServer = HttpServer(app)
    httpServer.bind_listen(8080)
    httpServer.start()



if __name__ == "__main__":
    main()