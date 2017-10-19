import test_import

fd = "./"
f = test_import.DirInfo(fd)
f.print_dir_pyfiles()
f_ = test_import.DirInfo("../")
f_.print_dir_pyfiles()
a = [1, "cc", ['s', 'a'], 2, 3, "sss"]
f_.print_list(a)
f_.print_list([1, 3, 5])
print "type(test_import): %s  -- type(f_): %s" % (type(test_import), type(f_))