import socket
import re
import multiprocessing


def service_client(new_tcp_server):
    """为客户端返回数据"""
    recv_data = new_tcp_server.recv(1024).decode("utf-8")
    #print(recv_data)
    request_lines = recv_data.splitlines()
    print("")
    print(">" * 20)
    print(request_lines)
    #1.准备给浏览器发送数据 ---header
    # GET /index.html HTTP/1.1
    # get post put del

    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)",request_lines[0])
    if ret:
        file_name = ret.group(1)
        # print("*"*50, file_name)
        if file_name == "/":
            file_name = "/index.html"

    try:
        f = open("./html" + file_name,"rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "------file not found-----"
        new_tcp_server.send(response.encode("utf-8"))
    else:
        file_content = f.read()
        f.close()
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        new_tcp_server.send(response.encode("utf-8"))
        new_tcp_server.send(file_content)
    new_tcp_server.close()



def main():
    #1.创建套接字
    tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #2.绑定套接字
    tcp_server.bind(("",7890))
    #3.将套接字设置成被动
    tcp_server.listen(128)
    #4.等待客户端发送请求
    while True:
        new_tcp_server,tcp_addr = tcp_server.accept()

        #5.给客户端返回数据
        p = multiprocessing.Process(target=service_client,args=(new_tcp_server,))
        p.start()
        new_tcp_server.close()
    tcp_server.close()


if __name__ == '__main__':
    main()