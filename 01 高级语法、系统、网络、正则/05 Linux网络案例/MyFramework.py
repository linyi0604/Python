import time


class Application(object):
    def __init__(self , u_list):
        self.url_list = u_list
    def __call__(self, env , start_response ) :
        '''

        :param environ: 是一个字典{}  eviron["file_name"] 用于存储环境变量 比如用户请求的文件、方法
        :param start_response: 是web服务器提供的一个回调函数callback
            参数 status的作用格式 设置响应行
            参数 header_nv_   是一个列表 每个元素是一个元组，每个元组两个元素 分别是相应头的key 和value（响应头的名称和值）
        :return: 返回的就是响应体
        '''
        header_list = [("Server", "HTTPServerByPython5.0")]
        # head_list.append()
        file_name = env["file_name"]

        # # /gettime/?name=tom
        for url , func in self.url_list:
            if file_name.startswith(url) and not file_name.endswith( ".py"):
                start_response("200 OK", header_list)
                return func()


        #如果.py结尾 作为动态资源请求处理
        if file_name.endswith(".py"):
            # import re 导入模块  能够使用re.match等方法，实际上python执行了下面
            # re = __import__("re")  返回了re的对象
            # import re  实际上是 re = __import__("re")
            # 前台传过来 "/gettime.py" 字符串
            try:
                module = __import__( file_name[1:-3] )   #截取出要导入的模块名字
            except ImportError as e :
                start_response("404 Not Found" , header_list)
                response_body =( "%s" % str(e) ).encode()
            else:
                start_response("200 OK" , header_list)
                response_body = module.application().encode()
        #否则当作静态请求
        else :
            try:
                HTML_ROOT_PATH = "."
                file_data = open( HTML_ROOT_PATH+file_name , "rb" )

            except FileNotFoundError as e:
                start_response("404 Not Found" , header_list)
                response_body = ("%s"%str(e)).encode()
            else:
                start_response("200 OK" , header_list)
                response_body = file_data.read()
                file_data.close()




        # start_response("200 OK", header_list)
        return response_body


def get_time():
    return time.ctime().encode()

def get_info():
    return "info:server by python".encode()

#路由列表
url_list = [
    (r"/gettime", get_time ),
    (r"/getinfo" , get_info ),
]



#app()
app = Application( url_list )