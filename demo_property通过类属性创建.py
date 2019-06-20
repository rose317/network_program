class Goods(object):
    def __init__(self):
        self.original_price = 100
        self.discount = 0.8

    def get_bar(self):
        new_price =  self.original_price * self.discount
        return new_price

    def set_bar(self,value):
        self.original_price = value


    def del_bar(self):
        del self.original_price


    BAR = property(get_bar,set_bar,del_bar)

obj = Goods()
print(obj.BAR)
obj.BAR = 200
print(obj.BAR)
del obj.BAR