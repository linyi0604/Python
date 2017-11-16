def app(environ, start_response):
    '''

    :param environ: 是一个字典{}  eviron["file_name"] 用于存储环境变量 比如用户请求的文件、方法
    :param start_response: 是web服务器提供的一个回调函数callback
        参数 status的作用格式 设置响应行
        参数 header_nv_   是一个列表 每个元素是一个元组，每个元组两个元素 分别是相应头的key 和value（响应头的名称和值）
    :return: 返回的就是响应体
    '''
    header_list = [("Server","HTTPServerByPython5.0")]
    #head_list.append()
    start_response( "200 OK" , header_list )
    return "Python Web Server!!!!!".encode()