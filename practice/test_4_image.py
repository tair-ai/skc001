#!/usr/bin/env python
# coding=utf-8

from skimage import io
import matplotlib.pyplot as plt

face = io.imread("test_img.jpg")
print face
print type(face)
plt.imshow(face)
plt.show()

