import socket


def send_msg(udp_socket):
    """发送数据"""
    dest_ip = input("请输入ip地址：")

    dest_port = int(input("请输入端口号："))

    send_data = input("请输入你要发送的内容：")
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def recv_msg(udp_socket):
    """接受数据"""
    recv_data = udp_socket.recvfrom(1024)
    print("%s:%s" % (recv_data[1], recv_data[0].decode("utf-8")))


def main():
    #创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定信息
    udp_socket.bind(("",7078))

    #使用循环进行数据处理
    while True:
        #创建聊天器功能选项
        print("-----聊天器-----")
        print("1.发送数据")
        print("2.接受数据")
        print("0.退出")
        op = input("请输入你的选择：")
        #发送数据
        if op == "1":
            send_msg(udp_socket)
        #接受数据
        elif op == "2":
            recv_msg(udp_socket)
        elif op == "0":
            exit()
        else:
            print("输入有误。请重新输入")

if __name__ == "__main__":
    main()