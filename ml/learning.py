# coding: utf-8

import sys
from sklearn import svm
import numpy as np

clf = svm.SVC(kernel='poly', degree=2, gamma=0.001, C=100.)

with file("train.txt") as f:
    f.next()                # 跳过第一行
    datas = []
    results = []
    for line in f:
        userid, itemid, rating = tuple([int(x) for x in line.split(',')])
        datas.append([userid, itemid])
        results.append(rating)
    clf.fit(datas, results)

with file("test.txt") as f:
    f.next()                # 跳过第一行
    for line in f:
        userid, itemid = tuple([int(x) for x in line.split(',')])
        arr = np.array([userid, itemid])
        rating = clf.predict(arr)
        sys.stdout.write(str(rating))
