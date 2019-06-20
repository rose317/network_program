import socket
import threading


def recv_msg(udp_socket):
    """接收数据"""
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)


def send_msg(udp_socket,dest_ip,dest_port):
    """发送数据"""
    while True:
        send_data = input("请输入你要发送的数据：")
        udp_socket.sendto(send_data.encode("utf-8"),(dest_ip, dest_port))


def main():
    #1.创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #2.绑定ip
    udp_socket.bind(("",7890))
    #3.获取对方ip/port
    dest_ip = input("请输入ip：")
    dest_port = int(input("请输入port："))

    #4.创建线程
    t1 = threading.Thread(target=recv_msg,args=(udp_socket,))
    t2 = threading.Thread(target=send_msg,args=(udp_socket,dest_ip,dest_port))
    t1.start()
    t2.start()



if __name__ == '__main__':
    main()