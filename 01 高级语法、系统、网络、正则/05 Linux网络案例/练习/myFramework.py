#encoding=utf-8

import time

class Application(object):
    def __init__(self , url_list ):
        self.url_list = url_list

    def __call__(self, env , set_response_head ):
        file_name = env["file_name"]
        head_list=[
            ("Host","Python Program Version 6.0"  )
        ]


        if file_name == "/":
            file_name = "/index.html"

        # 搜索路由表 优先执行路由表中的方法
        for file , func in url_list:
            if file_name == file:
                set_response_head("200 OK", head_list)
                return func()

        #查找动态文件
        if file_name.endswith(".py"):
            try :
                module = __import__( file_name[1:-3] )
            except ImportError as e:
                set_response_head("404 Not Found", head_list)
                response_body = str(e).encode()
            else :
                set_response_head("200 OK", head_list)
                response_body = module.application()
        #查找静态文件
        else :
            try :
                file = open( "."+file_name , "rb" )
            except FileNotFoundError as e:
                set_response_head("404 Not Found", head_list)
                response_body = str(e).encode()
            else:
                set_response_head("200 OK", head_list)
                response_body = file.read()
                file.close()

        return response_body



def get_time():
    return time.ctime().encode()

def get_info():
    return ("This is Python Program Server Version 6.0 " + time.ctime()).encode()
#定义路由表
url_list = [
    ("/gettime",get_time),
    ("/getinfo",get_info)
]

app = Application( url_list )