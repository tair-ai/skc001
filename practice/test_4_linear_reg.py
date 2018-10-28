#!/usr/bin/env python
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
real_func = lambda x: -2*x + 4
d1 = np.array(np.linspace(-4, 4, 1000))
d2 = real_func(d1) + .2 * np.random.normal(loc=0.0, scale=0.5, size=1000)
plt.scatter(d1, d2)
plt.show()

model =
