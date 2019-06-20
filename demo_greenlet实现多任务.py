from greenlet import greenlet
import time


def test_1():
    while True:
        print("---1--")
        #跳到test_2函数执行
        gr2.switch()
        time.sleep(0.5)


def test_2():
    while True:
        print("---2---")
        gr1.switch()
        time.sleep(0.5)
    

gr1 = greenlet(test_1)
gr2 = greenlet(test_2)

#跳到执行test_1函数
gr1.switch()