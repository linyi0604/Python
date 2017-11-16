'''
多进程服务器
'''
import socket
import multiprocessing

def handle_client(client_socket , client_address ):
    while True:
        data = client_socket.recv(1024)
        if len(data) > 0 :
            print(data.decode("utf-8"))
            #response = input("回复：")
            client_socket.send( data )
        else :
            print(client_address,"已下线!")
            client_socket.close()
            break



def main():
    server_socket = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
    server_socket.setsockopt( socket.SOL_SOCKET , socket.SO_REUSEADDR , 1 )
    server_socket.bind( ("",8080 )  )
    server_socket.listen( 128 )
    while True :

        client_socket , client_address = server_socket.accept()
        print(client_address,"已连接，交给子进程处理")
        #接收到的套接字交给子进程去处理
        p = multiprocessing.Process( target=handle_client, args=( client_socket, client_address ) )
        p.start()
        # 套接字交给子进程，子进程会复制引用 可以删除这个引用
        client_socket.close()



if __name__ == "__main__":
    main()