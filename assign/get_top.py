#!/usr/bin/env python
# coding=utf-8

#!/usr/bin/env python
# coding: utf-8
# vim: set et sw=4 ts=4 sts=4 fenc=utf-8

import os, time

time2sleep = 1

# cmd = "top -bi -n 1 -d 0.02 |grep {a}".format(a="mock_test")
cmd = "top  -n 1 -d 0.02 |grep {a}".format(a="12541")

print cmd

while True:
    ss = os.popen(cmd).read().split('\n')
    print ss
    if len(ss) > 1:
        d = ss[0]
        with open("log/new_test_bench_mark.log", "a") as f:
            print d
            f.write(d+"\n")
        time.sleep(time2sleep)

