'''
多线程服务器
'''
import socket
import threading
def handle_client(client_socket , client_address):
    while True:
        data = client_socket.recv(1024)
        if len(data) > 0 :
            print(data.decode())
            client_socket.send(input("回复").encode())
        else :
            print(client_address,"已下线！")
            break
    client_socket.close()

def main():
    server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    server.bind( ("",8080) )
    server.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1  )
    server.listen(128)
    while True:
        client_socket, client_address = server.accept()
        print(client_address,"已上线！交给子线程处理！")
        # 交给线程去处理，线程共享数据 所以不能关闭套接字
        handle_client( client_socket, client_address )




if __name__ == "__main__":
    main()