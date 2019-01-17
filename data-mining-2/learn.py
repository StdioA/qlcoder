import numpy as np
from sklearn.neighbors import KNeighborsClassifier


training_arr = np.loadtxt('train2.txt', str, '#', ' ')
testing_arr = np.loadtxt('check2.txt', str, '#', ' ')

arr_y = [[line[11]] for line in training_arr]
arr_x = [
    [float(x) for x in line[1:10]]
    for line in training_arr
]

testing_arr = [
    [float(x) for x in line[1:10]]
    for line in testing_arr
]

clf = KNeighborsClassifier(10)
clf.fit(arr_x, arr_y)
res_arr = clf.predict(testing_arr)

print(res_arr)
print("".join(map(str, res_arr)))
