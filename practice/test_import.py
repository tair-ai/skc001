#encoding: utf-8
import os

print "__EXEC__ IMPORT"
print __file__
print "__end__ import"

class DirInfo(object):
    def __init__(self, fdir):
        print ">>> EXEC INIT CLASS"
        self.file_dir = fdir

    def print_dir_pyfiles(self):
        print ">>> EXEC print pyfiles"
        files = os.listdir(self.file_dir)
        for f in files:
            if not f.endswith(".py"):
                continue
            else:print f

    def print_list(self, a):
        print ">>> EXEC print list"
        if isinstance(a, list):
            for i in range(len(a)):
                if isinstance(a[i], int):
                    print "[-] index: %d  %d" %(i , a[i])
