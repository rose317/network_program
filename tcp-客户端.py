import socket


def main():
    #创建tcp套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #链接服务器
    server_ip = input("请输入服务器ip：")
    server_port = int(input("请输入服务器port："))
    tcp_socket.connect((server_ip,server_port))
    #发送/接收数据
    send_data = input("请输入你要发送的内容:")
    tcp_socket.send(send_data.encode("utf-8"))
    #关闭套接字
    tcp_socket.close()

if __name__ == '__main__':
    main()