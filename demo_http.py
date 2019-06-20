from socket import *
import re
import gevent
from gevent import monkey

def server_client(new_socket):
    #接收数据，并utf-8进行解码
    recv_data = new_socket.recv(1024).decode("utf-8")
    #按行进行分隔
    request_line = recv_data.splitlines()
    print("")
    print(">" * 20)
    print(request_line)

    file_name = ""
    ret = re.match(r"[^/]+(/[^ ])",request_line[0])
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"

    try:
        f = open("./html/index.html","rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += ""
        response += "file not found"
        new_socket.send(response.encode("utf-8"))
    else:
        file_content = f.read()
        f.close()
        response = "HTTP/1.1 200 OK\r\n"
        response += ""
        new_socket.send(response.encode("utf-8"))
        new_socket.send(file_content)
    new_socket.close()


def main():
    #创建套接字
    tcp_socket = socket(AF_INET,SOCK_STREAM)
    #绑定ip，port
    tcp_socket.bind(("",7890))
    #将收听由主动设置为被动
    tcp_socket.listen(128)
    #等待客户端链接
    while True:
        new_socket,tcp_addr = tcp_socket.accept()
        #给客户返回数据
        gevent.spawn(server_client,new_socket)

    tcp_socket.close()

if __name__ == '__main__':
    main()