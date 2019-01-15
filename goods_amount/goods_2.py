# coding: utf-8

from collections import Counter
import sqlite3

goods = Counter()
db = sqlite3.connect("./goods.sqlite")
cur = db.cursor()

total = 0
f = file("goods_2.txt")
for no, line in enumerate(f):
    datas = line.split()
    if datas[0] == "up":
        num, price = int(datas[1]), int(datas[2])
        cur.execute("INSERT INTO goods (price, amount) VALUES (?, ?)", (price, num))
    elif datas[0] == "down":
        num, price = int(datas[1]), int(datas[2])
        cur.execute("INSERT INTO goods (price, amount) VALUES (?, ?)", (price, -num))
    else:
        count = 0
        low, high = int(datas[1]), int(datas[2])
        cur.execute("SELECT SUM(amount) FROM goods WHERE price>=? AND price<=?", (low, high))
        ans = cur.fetchone()[0]
        if ans is not None:
            total += ans
    if no % 1000 == 0:
        print no

f.close()
print total
