# coding: utf-8

import numpy as np
from matplotlib import pyplot as plt

px, py = [], []
with file("fitting_2.txt") as f:
    for line in f:
        x, y = tuple([float(x) for x in line.split()])
        px.append(x)
        py.append(y)

X, Y = np.array(px), np.array(py)
z1 = np.polyfit(X, Y, 5)
# p1 = np.poly1d(z1)

print ":".join([str(x) for x in z1])
