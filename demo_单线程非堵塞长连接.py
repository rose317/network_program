import socket
import re


#长链接作用减少服务器资源
def service_client(new_tcp_server,recv_data):
    """为客户端返回数据"""
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
        response_body = file_content
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"
        response = response_header.encode("utf-8") + response_body
        new_tcp_server.send(response)

    #new_tcp_server.close()



def main():
    #1.创建套接字
    tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #2.绑定套接字
    tcp_server.bind(("",7890))
    #3.将套接字设置成被动
    tcp_server.listen(128)
    tcp_server.setblocking(False)
    #4.等待客户端发送请求
    client_server_list = list()
    while True:
        try:
            new_tcp_server,tcp_addr = tcp_server.accept()
        except Exception as ret:
            pass
        else:
            new_tcp_server.setblocking(False)
            client_server_list.append(new_tcp_server)
        #5.给客户端返回数据
        for client_socket in client_server_list:
            try:
                recv_data = client_socket.recv(1024).decode("utf-8")
            except Exception as ret:
                pass
            else:
                if recv_data:
                    service_client(client_socket,recv_data)
                else:
                    client_socket.close()
                    client_server_list.remove(client_socket)

    tcp_server.close()


if __name__ == '__main__':
    main()