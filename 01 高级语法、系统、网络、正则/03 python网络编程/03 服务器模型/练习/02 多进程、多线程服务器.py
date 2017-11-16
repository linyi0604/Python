#coding=utf-8
import socket
import multiprocessing
import threading
# client 是一个列表 里面的元素是(socket,addr)
def handle_socket( client ):
    while True :
        data = client[0].recv(1024)
        if not data :
            print( client[1],"已经下线！" )
            client[0].close()
            break
        else:
            print(client[1], ":", data.decode())
            client[0].send(data)


# 对进程进行阻塞等待的功能
def join_process():
    for p in process :
        if not p.is_alive() :
            p.join()
            process_for_del.append(p)
    for p in process_for_del:
        process.remove(p)


#全局进程列表
process = []
process_for_del = []
if __name__ == "__main__":
    #开启一个socket
    server = socket.socket( socket.AF_INET ,  socket.SOCK_STREAM )
    #设置可重用地址
    server.setsockopt( socket.SOL_SOCKET , socket.SO_REUSEADDR , 1 )
    #绑定ip和端口
    server.bind( ( "", 8888 ) )
    #开启监听状态
    server.listen(128)
    while True:
        #接受客户端的连接
        client = server.accept()
        print(client[1],"已连接：")
        #交给进程或者线程处理连接业务
        p = multiprocessing.Process( target=handle_socket , args = (client, ) )
        p.start()
        process.append(p )
        join_process()