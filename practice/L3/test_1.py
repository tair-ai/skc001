#!/usr/bin/env python
# coding=utf-8

from test import *

a =  1234

if __name__ == "__main__":
    print a
    with open(sys.argv[1], "r") as fp:
        for i in fp.readlines():
            print i

