import socket


tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_server_socket.bind(("",7890))
tcp_server_socket.listen(128)
#设置非堵塞
tcp_server_socket.setblocking(False)
client_server_list = list()

while True:
    try:
        #接收数据
        new_socket,tcp_addr = tcp_server_socket.accept()
    except Exception as ret:
        print("还没有新用户链接")
    else:
        print("只要没有异常，就意味着来了一个用户")
        new_socket.setblocking(False)
        client_server_list.append(new_socket)

    for client_server in client_server_list:
        try:
            recv_data = client_server.recv(1024)
        except Exception as ret:
            print("用户还没有发送数据")
        else:
            print(recv_data)
            if recv_data:
                print("用户发送过来了数据")
            else:
                client_server.close()
                client_server_list.remove(client_server)
                print("客户端已经关闭")