import re

names = ["name","_name","2_name","__name__","name#name"]

for i in names:
    ret = re.match(r"[a-zA-Z_][a-zA-Z0-9_]*$",i)
    if ret:
        print("变量名%s符合要求" % i)
    else:
        print("变量名%s非法" % i)