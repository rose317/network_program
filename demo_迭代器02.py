import time


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.num = 0

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < len(self.names):
            ret = self.names[self.num]
            self.num += 1
            return ret
        else:
            raise StopIteration

        
classmate = Classmate()
classmate.add("rose")
classmate.add("jordan")
classmate.add("kobe")

for name in classmate:
    print(name)
    time.sleep(1)