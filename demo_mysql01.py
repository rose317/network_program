from pymysql import *


class JD(object):
    def __init__(self):
        self.conn = connect(host='localhost',port=3306,user='root',
                            password='derrick01',database='jing_dong',charset='utf8')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def execute_sql(self,sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_items(self):
        """显示所有商品"""
        sql = "select * from goods;"
        self.execute_sql(sql)

    def show_cate(self):
        sql = "select name from goods_cates;"
        self.execute_sql(sql)

    def show_brands(self):
        sql = "select name from goods_brands;"
        self.execute_sql(sql)

    def add_brand(self):
        item_name = input("请输入你要添加的品牌：")
        sql = """insert into goods_brands (name) value("%s")""" % item_name
        self.cursor.execute(sql)
        self.conn.commit()

    def get_info_by_name(self):
        find_name = input("请输入要查询的商品名字：")
        sql = "select * from goods where name = %s"
        self.cursor.execute(sql,[find_name])
        print(self.cursor.fetchall())

    def buy_goods(self):
        good_name = input("请输入要购买的商品：")
        name = input("请输入你的用户名：")
        sql_id = "select id from customer where name = '%s'" % name
        sql_good_id = "select id from goods where name = '%s'" % good_name
        self.cursor.execute(sql_id)
        id = 0
        for temp in self.cursor.fetchone():
            id = temp
            print(id)
        self.cursor.execute(sql_good_id)
        good_id = 0
        for temp1 in self.cursor.fetchone():
            good_id = temp1
            print(good_id)
        sql = """insert into orders value('%s');""" % id
        sqln = """insert into order_detail (0,'%s','%s',4);""" %(id,good_id)
        self.cursor.execute(sql)
        self.cursor.execute(sqln)
        self.conn.commit()


    @staticmethod
    def show_menu():
        print("----京东----")
        print("1.查询所有的商品")
        print("2.查询所有商品分类")
        print("3.查询所有商品品牌分类")
        print("4.添加商品品牌")
        print("5.查询想要查询的商品")
        print("6.商品下单")
        return input("请输入你需要进行的操作：")

    def run(self):
        while True:
            num = self.show_menu()
            if num == "1":
                #查询所有商品
                self.show_all_items()
            elif num == "2":
                #查询分类
                self.show_cate()
            elif num == "3":
                #查询品牌
                self.show_brands()
            elif num == "4":
                self.add_brand()
            elif num == "5":
                #根据名字查询商品
                self.get_info_by_name()
            elif num == "6":
                self.buy_goods()
            else:
                print("你的选择错误，请进行其他操作")

    def new_user(self):
        while True:
            name = input("请输入你要创建的名字：")
            sql = "select name from customer;"
            self.cursor.execute(sql)
            list1 = []
            for temp in self.cursor.fetchall():
                list1 = temp
            if name in list1:
                print("用户名已经存在，请重新输入")
                continue
            else:
                break
        pwd = input("请输入密码:")
        adr = input("请输入你的地址：")
        tel = input("请输入你的电话号码：")
        sql1 = """insert into customer values (0,'%s','%s','%s','%s')""" % (name,adr,tel,pwd)
        self.cursor.execute(sql1)
        self.conn.commit()

    def old_user(self):
        name = input("请输入你的用户名：")
        pwd = input("请输入你的密码：")
        sql = """select passwd from customer where name = '%s'""" % name
        self.cursor.execute(sql)
        passwd = ''
        for temp in  self.cursor.fetchone():
            passwd = temp
        if passwd == pwd:
            self.run()
        else:
            print("密码输入错误")

    def show_main_menu(self):
        while True:
            print("1.登陆")
            print("2.注册")
            choice = input("请输入你要进行的操作：")
            if choice == "1":
                self.old_user()
            elif choice == "2":
                self.new_user()
            else:
                print("请重新选择")

def main():
    jd = JD()
    jd.show_main_menu()



if __name__ == '__main__':
    main()