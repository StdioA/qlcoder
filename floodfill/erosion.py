# coding: utf-8

from skimage import io, color
import skimage.morphology as sm
import matplotlib.pyplot as plt
import numpy as np


# def generate_erosed(img):
#     grayimg = color.rgb2gray(img)
#     dst = grayimg
#     # dst = sm.erosion(dst,sm.square(6))
#     dst = sm.erosion(dst,sm.disk(6))
#     io.imsave("floodfill_erosed.png", dst)
#     return dst

# dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

# start_point = (512, 514)
# route = [start_point]
# img = io.imread("floodfill.png")
# dst = generate_erosed(img)
img = io.imread("034Z3fG.png")

def find(p, d=0):
    global route
    x, y = p

    if dst[x, y] == 0.0 or dst[x, y] == 1.0:
        return -1
    
    dst[x, y] = 1.0

    for i, di in enumerate(dirs[d:]+dirs[:d]):
        dx, dy = di
        if 0.0<dst[x+dx, y+dy]<1.0:
            route.append((x+dx, y+dy))
            return i

    print "Didn't find"
    return -1

# dst *= 4
# io.imsave("f.bmp", dst)

# td = find(route[-1])
# while td != -1:
#     td = find(route[-1], td)

# print len(route)
# print route
# cp = np.zeros(dst.shape, dtype=int)
# for x, y in route:
#     cp[x, y] = 1

# plt.subplot(121)
# plt.imshow(cp)
# plt.subplot(122)
# plt.imshow(dst)
# plt.show()
