import socket


#创建文件内容发送至客服端
def send_file_2_client(new_tcp_socket,socket_addr):
    # 接收数据并解码
    file_name = new_tcp_socket.recv(1024).decode("utf-8")
    print("客户端[%s]需要接受的文件：%s" % (str(socket_addr),file_name))

    #读取文件要发送的内容
    file_content = None
    try:
        f = open(file_name,"rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("无法打开文件")
    #如果有内容再发送给客户端
    if file_content:
        new_tcp_socket.send(file_content)

def main():
    #1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #2.绑定服务器ip/port
    tcp_server_socket.bind(("",7890))
    #3.将服务器监听由主动设置为被动
    tcp_server_socket.listen(128)
    while True:
        #4.等待客户端链接
        new_tcp_socket,socket_addr = tcp_server_socket.accept()

        #5.接收客户端输入并发送文件去客户端
        send_file_2_client(new_tcp_socket,socket_addr)

        #6.关闭套接字
        new_tcp_socket.close()
    tcp_server_socket.close()

if __name__ == '__main__':
    main()