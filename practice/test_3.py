#encoding: utf-8
import os
# 打印.Py文件
print [i for i in os.listdir("./") if i.endswith(".py")]

# 打印txt的内容
with open("test_3.txt", "r+") as f: print [i for i in f.readlines()]

# 导入pprint
import pprint
[pprint.pprint(i) for i in os.listdir("./") if i.endswith(".py")]

# 定义打印函数
def print_(s):print s
with open("test_3.txt", "r+") as f:[print_(i) for i in f.readlines()]

# 将查找的 py，文件写入一个txt文件
with open("test_3_write.txt", "w+") as f:
    [f.writelines(i + "\n") for i in os.listdir("./") if i.endswith(".py")]
    # map(lambda x: f.writelines(x + "\n"), [i for i in os.listdir("./") if i.endswith(".py")])

try:
    print b
except NameError, e:
    print e
