from socket import *


def main():
    #1.创建套接字
    tcp_socket = socket(AF_INET,SOCK_STREAM)
    #2.获取ip/port
    dest_ip = input("请输入ip：")
    dest_port = int(input("请输入port："))
    #3.链接服务器
    tcp_socket.connect((dest_ip,dest_port))
    #4.获取下载的文件名
    file_name = input("请输入要下载的文件名：")
    #5.将下载的名字传入服务器
    tcp_socket.send(file_name.encode("utf-8"))
    #6.接收数据
    recv_data = tcp_socket.recv(1024)
    #7.将接收的数据写入并保存
    if recv_data:
        with open("[新]"+file_name,"wb") as f:
            f.write(recv_data)
    #8.关闭套接字
    tcp_socket.close()

if __name__ == '__main__':
    main()