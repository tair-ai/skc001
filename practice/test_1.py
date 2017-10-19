#!/usr/bin/env python
# encoding: utf-8

# !/usr/bin/env python          ,声明解释器,不必须; 井号为注释，即井号注释代码段不会运行
# encoding: utf-8               ,声明源码编码格式，如果源码含有中文字符，去掉该声明则程序会报错

def print_a(a):         # 定义函数开始，def 为定义标识符，print_a 为函数名(标识符命名规则)，a为参数变量
    print "ENTER print_a(a） >>>>>>>>>>>>"
    print a             # 执行打印变脸函数  等价于 print a.__repr__()，:后的程序块需要严格4空格缩进格式
    s = dir(a)          # s 为局部变量，函数体内如果定义,if中的s定义在此处无效
    print "-> type(s): ", type(s), "=== len(s): %d" % len(s) # % 为字符串格式操作符
    print s[34:44]
    print "-> id(a): ", id(a), 
    print a.__repr__()# 调用类型对象的方法，该方法为内建方法(所有类型都有)，使用 . 操作符调用
    print b             # 未定义变量b，程序报错(抛出异常)，如果没有捕获异常情况下，则中断整个进程 

print ">>>>"  # 不缩进，函数体结束, 改语句在文件载入运行

if __name__ == "__main__": # 文件执行入口，当该文件作为被执行文件时，执行其body的程序块，:后紧跟程序段的body
                           # if 为判断语句声明，== 为想定判断，该语句为判断 __name__ 变量为主函数类型
    print "ENTER __MAIN___ >>>>>>>>>>>>"
    c, s = globals(), 1    # 定义变量并赋值, 等号为赋值操作符，声名多个变量使用”,“操作符号      
    print type(s)          # 查看类型对象的方法，直接调用，dir / type 等为解释器内建方法，可直接调用
    print type(c), c["__name__"], c.keys() # 查看c的类型，取字典的某个key的值，调用字典对象的keys()方法
    print id(s)            # 变量的对象地址，参照传参对象地址
    print_a(s)             # 调用定义的函数，需要安装函数变量模式进行传参
    print_a(s, s)          # 不按规定传参，会报错；由于上一句执行出错，因此不会执行到这一句
