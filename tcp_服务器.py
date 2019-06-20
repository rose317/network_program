import socket


def main():
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.绑定ip
    tcp_server_socket.bind(("", 7890))
    # 3.让默认的套接字由主动变为被动
    tcp_server_socket.listen(128)
    # 4.等待客户端链接
    while True:
        new_tcp_socket, socket_addr = tcp_server_socket.accept()
        # 5.接受/发送数据
        while True:
            recv_data = new_tcp_socket.recv(1024)
            if recv_data:
                print(recv_data)
                new_tcp_socket.send("hhhhaaaa".encode("utf-8"))
            else:
                break
        # 6.关闭所有套接字
        new_tcp_socket.close()

    tcp_server_socket.close()



if __name__ == '__main__':
    main()
