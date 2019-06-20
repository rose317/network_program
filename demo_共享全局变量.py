import threading
import time

#共享全局变量和传入参数
g_nums = [11,22]

def test1(temp):
    temp.append(33)
    print("test1---%s" % str(temp))


def test2(temp):
    print("test2---%s" % str(temp))

def main():
    t1 = threading.Thread(target=test1,args=(g_nums,))  #用args传入参数，形式为元组，参数后面加逗号
    t2 = threading.Thread(target=test2,args=(g_nums,))
    t1.start()
    time.sleep(2)
    t2.start()
    time.sleep(2)


if __name__ == '__main__':
    main()
