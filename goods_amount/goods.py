# coding: utf-8

from collections import Counter

goods = Counter()

total = 0
f = file("goods.txt")
for line in f:
    datas = line.split()
    if datas[0] == "up":
        num, price = int(datas[1]), int(datas[2])
        goods[price] += num
    elif datas[0] == "down":
        num, price = int(datas[1]), int(datas[2])
        goods[price] -= num
    else:
        count = 0
        low, high = int(datas[1]), int(datas[2])
        for p in range(low, high+1):
            count += goods[p]
        total += count

f.close()
print total
