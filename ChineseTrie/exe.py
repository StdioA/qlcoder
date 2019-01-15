# coding: utf-8

import sys

def diff(s1, s2):
    l1, l2 = len(s1), len(s2)
    minl, maxl = min(l1, l2), max(l1, l2)

    i = 0
    while i<minl:
        if s1[i] != s2[i]:
            break
        i += 1

    return l2-i


def sort_key(s):
    return len(s), s


def main():
    strs = []
    for line in sys.stdin:
        if line:
            strs.append(line.strip().decode('gbk'))
    strs.sort()
    
    length = len(strs)
    node = 1+len(strs[0])

    for i in range(1, length):
        node += diff(strs[i], strs[i-1])

    return node


if __name__ == '__main__':
    print main()
