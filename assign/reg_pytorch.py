#!/usr/bin/env python
# coding: utf-8
# vim: set et sw=4 ts=4 sts=4 fenc=utf-8
# Author: nasa
# Created: 2017-05-26 10:39 CST

from itertools import count
import torch
import torch.autograd
import torch.nn.functional as F
from torch.autograd import Variable
import matplotlib.pyplot as plt

POLY_DEGREE = 4
W_target = torch.randn(POLY_DEGREE, 1) * 5
b_target = torch.randn(1) * 5


def make_features(x):
    x = x.unsqueeze(1)
    return torch.cat([x ** i for i in range(1, POLY_DEGREE+1)], 1)

def f(x):
    return x.mm(W_target) + b_target[0]

def get_batch(batch_size=32):
    random = torch.randn(batch_size)
    x = make_features(random)
    y = f(x)
    return Variable(x), Variable(y)


fc = torch.nn.Linear(W_target.size(0), 1)

for batch_idx in count(1):
    batch_x, batch_y = get_batch()
    fc.zero_grad()

    output = F.smooth_l1_loss(fc(batch_x), batch_y)
    loss = output.data[0]
    output.backward()

    for param in fc.parameters():
        param.data.add_(-0.1 * param.grad.data)
        print loss
    if loss < 1e-3:
        break


