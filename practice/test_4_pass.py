#!/usr/bin/env python
# coding=utf-8

def test_pass(data):
    print id(data)
    if isinstance(data, list):
        data[0] = "test_list"
    if isinstance(data, dict):
        data['test'] = "dict"

if __name__ == "__main__":
    a = [1, 2, 3, 4]
    print id(a)
    test_pass(a)
    print a
    b = "sss"
    print id(b)
    test_pass(b)
    c = {"a": 1, "b": 2}
    print id(c)
    test_pass(c)
    print c
    d = 2
    print id(d)
    test_pass(d)
    print d

