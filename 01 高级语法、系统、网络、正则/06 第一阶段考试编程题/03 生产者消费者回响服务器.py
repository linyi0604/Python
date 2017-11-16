'''
编写一个基于tcp的echo服务器(回响服务器，即将客户端发送的信息返回给客户端)，
要求使用线程和生产者消费者模型（提示：一个线程accept--生产者；两个线程用于接收和发送--消费者）。
'''
import socket
import queue
import threading

#生产者工作函数，用于accept客户端的socket连接,传入客户端的socket和消息队列
def producer( server_socket , queue ):
    while True:
        #接收客户端的连接
        client_socket , client_address = server_socket.accept()
        #提示一下客户端连接了我们的服务器
        print(client_address,"已连接！")
        #如果消息队列满了就阻塞等待队列 把socket和address以元组形式放进队列
        queue.put( (client_socket , client_address) ,True)


#消费者工作函数，用于接收客户端消息并回复响应
def customer( queue ):
    while True:
        #阻塞等待取出队列中的客户端socket和地址
        client_socket , client_address = queue.get(True)
        #接收客户端连接之后 一直与它收发信息
        while True:
            #接收客户端发来的消息
            data = client_socket.recv(2048)
            #如果客户端请求断开,那么我们就断开,继续执行任务
            if not data:
                break
            #打印客户端发来的消息
            print(client_address,"发来消息：",data.decode())
            #将消息进行回复给客户端 回响
            client_socket.send(data)
        #业务结束关闭客户端套接字 进行下一次执行任务
        print(client_address,"已经下线！")
        client_socket.close()



def main():
    #创建一个消息队列,里面能存放100条消息 用于生产者和消费者之间通信
    q = queue.Queue(100)

    #创建套接字 指明用于互联网通信 流式tcp协议
    server_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    #设置地址重用
    server_socket.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
    #绑定端口
    server_socket.bind( ("", 8080) )
    #开启监听状态
    server_socket.listen(128)

    #生产者 接收客户端连接的线程
    accThread = threading.Thread( target=producer, args=(server_socket, q) )
    accThread.start()
    # 开启两个消费者 用于读取客户端发来的消息并回复
    for i in range(2):
        thread = threading.Thread( target=customer ,args=( q, ) )
        thread.start()


    #遍历当前所有线程进行阻塞等待
    for thread in threading.enumerate():
        if thread is not threading.current_thread():
            thread.join()

if __name__ == "__main__":
    main()