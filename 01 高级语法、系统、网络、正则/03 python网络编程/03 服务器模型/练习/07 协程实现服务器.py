#coding=utf-8
import socket
import gevent

gevent.monkey.patch_all()
def handle_client( client, addr ):
    while True:
        data = client.recv(1024)
        if not data:
            print(addr,"下线！")
            client.close()
            break
        else :
            print(addr,":",data.decode())
            client.send(data)


def server(port):
    server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    server.setsockopt( socket.SOL_SOCKET , socket.SO_REUSEADDR , 1 )
    server.bind( "",port )
    server.listen(128)
    while True:
        client, addr = server.accept()
        print(addr,"上线！")
        handle_client( client, addr )



if __name__ == "__main__":
    server(8888)