# coding: utf-8

import numpy as np
from matplotlib import pyplot as plt

px, py = [], []
with file("fitting.txt") as f:
    for line in f:
        x, y = tuple([float(x) for x in line.split()])
        px.append(x)
        py.append(y)

X, Y = np.array(px), np.array(py)


# plt.scatter(X, Y)
# plt.show()

z1 = np.polyfit(X, Y, 1)
p1 = np.poly1d(z1)

print z1
print p1
