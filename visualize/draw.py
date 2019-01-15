# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np

px = np.zeros(10006)
py = np.zeros(10006)

with file("plots.txt", "r") as f:
    for i, line in enumerate(f):
        x, y = tuple(map(int, line.split()))
        px[i], py[i] = x, 400-y

plt.scatter(px, py)
plt.show()
