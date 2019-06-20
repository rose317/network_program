import time


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        #返回一个对象，用self指向对象classmata
        return ClassIterator(self)


class ClassIterator(object):
    def __init__(self,obj):
        self.obj = obj
        self.num = 0
    #创建迭代器的对象里必须有iter 和 next函数
    def __iter__(self):
        pass

    def __next__(self):
        if self.num < len(self.obj.names):
            ret = self.obj.names[self.num]
            self.num += 1
            return ret
        else:
            #当迭代完后抛出一个停止异常
            raise StopIteration

classmate = Classmate()
classmate.add("rose")
classmate.add("jordon")
classmate.add("kobe")

for name in classmate:
    print(name)
    time.sleep(1)