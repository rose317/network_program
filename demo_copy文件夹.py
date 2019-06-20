import os
import multiprocessing


def copy_txt(q,file_name,old_folder_name,new_folder_name):
    """完成文件的复制"""
    #1.获取源文件路径
    old_f = open(old_folder_name + '/'+ file_name,"rb")
    #2.读取数据
    content = old_f.read()
    #3.关闭原文件夹
    old_f.close()
    #4.创建一个新文件
    new_f = open(new_folder_name + '/'+ file_name,"wb")
    #5.写入数据
    new_f.write(content)
    #6.关闭新文件夹
    new_f.close()
    q.put(file_name)


def main():
    #1.输入需要拷贝的文件夹
    old_folder_name = input("请输入需要拷贝的文件夹：")
    #2.创建新的文件夹
    try:
        new_folder_name = old_folder_name + "[复件]"
        os.mkdir(new_folder_name)
    except:
        pass

    #3.读取拷贝文件夹中所有文件
    file_names = os.listdir(old_folder_name)
    #4.创建进程池
    po = multiprocessing.Pool(5)
    #5.创建一个队列
    q = multiprocessing.Manager().Queue()
    #6.向进程池中添加所有文件
    for file_name in file_names:
        po.apply_async(copy_txt,args=(q,file_name,old_folder_name,new_folder_name))

    po.close()
    all_fill_num = len(file_names)
    finish_copy = 0
    while True:
        file_name1 = q.get()
        #print("已完成copy %s" %file_name1)
        finish_copy += 1
        print("\r进度为 %.2f %%" %(finish_copy*100/all_fill_num),end="")
        if finish_copy >= all_fill_num:
            break


if __name__ == '__main__':
    main()