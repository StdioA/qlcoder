# coding: utf-8

import sys
import time
from sklearn import svm
from sklearn import ensemble
import numpy as np

clf = svm.SVC(kernel='poly', degree=2, gamma=0.001, C=100.)
# clf = ensemble.RandomForestClassifier()

datas = []
results = []

print "Program Started", time.ctime()
with file("train.txt") as f:
    for line in f:
        data_l = line.split()

        datas.append([float(x) for x in data_l[1:-1]])
        results.append(int(data_l[-1]))

print "Reading Complete", time.ctime()
datas, results = np.array(datas), np.array(results)
clf.fit(datas, results)
print "Training Complete", time.ctime()


final = []

with file("check.txt") as f:
    for line in f:
        data_l = line.split()

        data = [float(x) for x in data_l[1:]]
        f_r = clf.predict(data)
        final.append(f_r)
        sys.stdout.write(str(f_r))

with file("result.txt", "w") as f:
    f.write("".join([str(x) for x in final]))
