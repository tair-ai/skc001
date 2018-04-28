#!/usr/bin/env python
# coding=utf-8

from skimage import io
import matplotlib.pyplot as plt
import numpy as np
face = io.imread("test_img.jpg")
print face
print type(face)
print face.shape
plt.imshow(face)
plt.show()
gray_img = 0.299 * face[:,:,0] + 0.587 * face[:,:,1] + 0.114 * face[:,:,2]
gray_img = gray_img.astype(np.uint8)
print gray_img.shape
plt.imshow(gray_img)
plt.show()
io.imsave("test_4_new.jpg", gray_img)
plt.hist(gray_img.flatten())
plt.show()
