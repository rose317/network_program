#使用互斥锁解决全局变量资源竞争问题
import threading
import time


#创建一个锁对象
mutex = threading.Lock()
g_num = 0
def test1(num):
    global g_num
    #互斥锁上锁
    mutex.acquire()
    for i in range(num):
        g_num += 1
    #解除锁
    mutex.release()
    print("g_num的数值为%d" % g_num)


def test2(num):
    global g_num
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()
    print("g_num的数值为%d" % g_num)

def main():
    t1 = threading.Thread(target=test1,args=(1000000,))
    t2 = threading.Thread(target=test2,args=(1000000,))
    t1.start()
    t2.start()
    time.sleep(2)
    print("g_num数值为%d" % g_num)


if __name__ == '__main__':
    main()