# coding: utf-8

with file("1.txt") as f:
    print "-".join([l.strip() for l in f])
