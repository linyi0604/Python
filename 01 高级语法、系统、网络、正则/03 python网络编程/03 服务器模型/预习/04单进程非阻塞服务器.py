'''
单线程 非阻塞的服务器
'''
import socket

#开启一个列表 里面存储接收到的新客户端的套接字和地址的列表
client_list = [ ]
def main():
        # 1 设置一个套接字 指明 互联网通信  流式运用tcp协议
        server_socket = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
        # 2 绑定地址和端口
        server_address = ( "",8080 )
        server_socket.bind( server_address )
        # 3 设置重用地址
        server_socket.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR ,1 )
        # 4 开启监听状态
        server_socket.listen(128)
        # 5 设置非阻塞
        server_socket.setblocking(False)
        # 6 接收客户端的连接请求
        # 设置非阻塞的时候 如果有多个客户端同时来链接 会抛出异常
        while True:
                try :   #将获取的客户端放入列表 等待处理
                        client = server_socket.accept()
                        client[0].setblocking(False)
                        client_list.append(client )
                except :
                        pass
                #处理完成的客户端放在里面
                del_client_list = []
                # 对收到连接的客户端业务进行处理
                for client in client_list:
                        try:
                                # client 里面是 客户端套接字和地址的元组
                                while True:
                                        data = client[0].recv(1024)
                                        if len(data)> 0:

                                                print(client[1],":",data.decode("utf-8"))
                                                client[0].send(input("回复：").encode("utf-8"))
                                        else :
                                                print(client[1],"已下线！")
                                                break
                                client[0].close()
                                del_client_list.append(client)
                        except :
                                pass
                # 处理要删除的客户端
                for client in del_client_list:
                        del_client_list.remove(client)

if __name__ == "__main__":
        main()


