#encoding: utf-8
import os
# 打印.Py文件
print [i for i in os.listdir("./") if i.endswith(".py")]

# 打印txt的内容
with open("test_2.txt", "r+") as f: print [i for i in f.readlines()]

# 导入pprint
import pprint
[pprint.pprint(i) for i in os.listdir("./") if i.endswith(".py")]

# 定义打印函数
def print_(s):print s
with open("test_2.txt", "r+") as f:map(lambda x: print_(x),  [i for i in f.readlines()])