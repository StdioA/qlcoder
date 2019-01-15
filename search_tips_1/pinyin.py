# coding: utf-8

from pypinyin import lazy_pinyin

f = file("search.txt")
pyl = []
for line in f:
    line = line.strip().decode("utf-8")
    pyl.append("".join(lazy_pinyin(line)))

print "\n".join(pyl)
