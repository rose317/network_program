import re


def main():
    Email_adr = input("请输入你的邮箱：")

    ret = re.match(r"[a-zA-Z_0-9]{4,20}@163\.com$",Email_adr)
    if ret:
        print("邮箱%s符合要求" % Email_adr)
    else:
        print("邮箱%s不符合要求" % Email_adr)

if __name__ == '__main__':
    main()