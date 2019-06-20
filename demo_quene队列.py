import multiprocessing


def download_data(q):
    #创建一个数据
    data = [11,22,33,44]
    #读取数据
    for temp in data:
        q.put(temp)
    print("数据下载完成")


def analysis_data(q):
    #创建存储数据列表
    wait_data = list()
    while True:
        data = q.get()
        wait_data.append(data)
        if q.empty():
            break
    print(wait_data)


def main():
    #创建queue队列
    q = multiprocessing.Queue()
    #创建进程
    p1 = multiprocessing.Process(target=download_data,args=(q,))
    p2 = multiprocessing.Process(target=analysis_data,args=(q,))
    p1.start()
    p2.start()

if __name__ == '__main__':
    main()