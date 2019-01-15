# coding: utf-8


def bwt(s):
    """对字符串进行Burrows-Wheeler变换 不使用唯一字符('EOF')做标记 返回索引值列表"""
    #创建所有循环字符串
    table = [s[i:] + s[:i] for i in range(len(s))]
    #获取排序后的结果
    table_sorted = table[:]
    table_sorted.sort()
    #获取已排序表每个字符串在未排序表中对应字符串的下一个字符串在已排序表中的索引值
    indexlist = []
    for t in table_sorted:
        index1 = table.index(t)
        index1 = index1+1 if index1 < len(s)-1 else 0
        index2 = table_sorted.index(table[index1])
        indexlist.append(index2)
    #取排序后结果的最后一列作为结果字符串
    r = ''.join([row[-1] for row in table_sorted])
    return r, indexlist

def ibwt(r,indexlist):
    """对字符串进行反Burrows-Wheeler变换 有索引值的反变换比使用唯一标记的反变换简单很多"""
    s=''
    x = indexlist[0]
    for _ in r:
        x = indexlist[x]
        s = s + r[x]
    return s

# print bwt("^bananabananabanana|")
print bwt("^BABABABANANABABABABABANANABABABABABANANABANANANAAHH|")[0]
