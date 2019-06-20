import threading


#使用类定义线程方法，必须定义run方法
class MyThread(threading.Thread):
    def run(self):
        print("这是run方法")

    def login(self):
        print("这是登陆方法")



if __name__ == '__main__':
    t = MyThread()
    t.start()   #自动调用类里面的run方法/login方法不会被自动调用
                #要想调用login方法，可以将login方法调用在run方法里面
