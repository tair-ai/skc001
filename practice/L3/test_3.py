#!/usr/bin/env python
# coding=utf-8

import os

fp = "data"
fl = os.listdir(fp)
print fl
jl = [os.path.join(".", i) for i in fl]
print jl
