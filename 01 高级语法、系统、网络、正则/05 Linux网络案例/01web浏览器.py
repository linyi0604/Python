'''
模拟浏览器下载 http://www.itcastcpp.cn 主页

1 创建tcp链接
2 组装请求报文 并且发送
3 接收web服务器的响应报文
4 关闭tcp 连接

'''
import socket



def main():
    # 1 创建tcp链接 inet对应ipv3  stream流式对应tcp链接
    #与服务器进行通信的socket
    server_socket = socket.socket( socket.AF_INET , socket.SOCK_STREAM )

    # 2 连接远程主机
    #ip或者域名为要连接的地方  端口80 默认为http协议的端口
    server_address=("192.168.85.81", 80 )
    server_socket.connect( server_address )

    # 3 构造请求报文 并发送
    #第一行   方法  路径   协议版本 换行符
    request_line = "GET /index2.html HTTP/1.1\r\n"
    request_head = "Host: 192.168.85.81\r\n"
    #请求体    请求行  + 请求头 + 一个空行   如果不是get方法 还 要加上请求体
    request_data = request_line + request_head + "\r\n"

    #发送 转换成字节码格式 默认utf-8格式
    server_socket.send( request_data.encode() )

    # 4 接收http报文
    response_data =  server_socket.recv(1024)
    #print( response_data.decode() )
    # 解码成字符串
    response_string_data = response_data.decode()
    #找到响应头的结尾位置，也就是响应体的开始位置，也就是取回来的网页开始的位置
    body_start_index = response_string_data.find( "\r\n\r\n" ) + 4
    print(response_string_data[body_start_index:])



if __name__=="__main__":
    main()