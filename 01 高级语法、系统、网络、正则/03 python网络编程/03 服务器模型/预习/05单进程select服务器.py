#coding:utf8
# import select
# import socket
# import sys
#
# server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
# server.bind( ("", 8080 ) )
# server.listen(5)
#
# inputs = [ server, sys.stdin ]
#
# running = True
#
# while True:
#     #调用select函数 阻塞等待
#     readable , writeable , exceptional = select.select( inputs ,[],[] )
#     # 数据抵达， 循环
#     for sock in readable:
#         #监听到有链接的进程
#         if sock == server :
#             conn, addr = server.accept()
#             # select 监听socket
#             inputs.append(conn)
#         #监听键盘有输入
#         elif sock == sys.stdin :
#             cmd = sys.stdin.readline()
#             running = False
#             break
#         # 有数据抵达
#         else :
#             #读取客户端链接发送的数据
#             data = sock.recv(1024)
#             if data :
#                 sock.send(data)
#             else :
#                 # 移除select监听的socket
#                 inputs.remove(sock)
#                 sock.close()
#     # 如果检测到用户输入敲击键盘 就退出
#     if not running :
#         break
# server.close()


'''
另一个服务器 包含writeList
'''
import socket
import queue
import select

SERVER_IP = ( "", 8080 )

# 保存客户端发送过来的消息，将消息存放到队列中
message_queue = { }
input_list = [ ]
output_list = [ ]

if __name__ == "__main__":
    server = socket.socket()
    server.bind(SERVER_IP)
    server.listen(10)
    #设置为非阻塞
    server.setblocking(False)

    input_list.append(server)

    while True:
        # 开始 select监听 对input_list 中的服务端server进行监听
        stdinput , stdoutput , stderr = select.select( input_list , output_list , input_list )
        # 循环判断是否有客户端连接进来 当有客户端链接进来时候select将触发
        for obj in stdinput:
            #判断当前触发的是不是服务器对象
            #当触发的是服务器对象 说明有新客户端连接起来了
            if obj == server :
                #接收客户端的链接 获取客户端对象和客户端地址
                conn , addr = server.accept()
                print(addr,"已连接")
                #将客户端加入到监听列表当中，当客户端发送消息时select将触发
                input_list.append(conn)
                # 为连接的客户端单独创建消息队列 用来保存客户端发送的消息
                message_queue[conn] = queue.Queue()
            else :
                #由于客户端连接进来时服务器收到客户端连接请求，将客户端加入到了监听列表中，
                #客户端发送笑傲系会触发，所以判断是否是客户端对象触发
                try:
                    recv_data = obj.recv(1024)
                    #客户端为断开
                    if recv_data :
                        print(addr,"已连接：",recv_data)
                        #将收到的消息放入客户端的消息中
                        message_queue[obj].put(recv_data)

                        #将回复操作放到output列表中 让select监听
                        if obj not in output_list:
                            output_list.append(obj)
                except :#ConnectionResetError :
                    #客户端断开连接了，将客户端的监听从input列表移除
                    input_list.remove(obj)
                    #移除消息队列
                    del message_queue[obj]
                    print(addr,"失去链接！")
            #如果没有客户端请求 也没有客户端发送消息 开始对发送消息队列进行处理 是否要发送消息
            for sendobj in output_list:
                try:
                    #如果消息队列中有消息，从消息队列中获取要发送的消息
                    if not message_queue[sendobj].empty():
                        #从消息队列中获取消息发送
                        send_data = message_queue[sendobj].get()
                        sendobj.send(send_data)
                    else :
                        # 将监听移除 等待下一次客户端发送消息
                        output_list.remove(sendobj)

                except ConnectionResetError:
                    #客户端断开了链接
                    del message_queue[sendobj]
                    output_list.remove(sendobj)
                    print(addr,"失去连接！")

