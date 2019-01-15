# coding: utf-8

def br2int(br):
    num = 0
    for x in br:
        num = (num<<8)+x
    return num

with file("rf.data", "rb") as ori_file:
    data = bytearray(ori_file.read())

count = 0
p = 0

while p < len(data):
    status = data[p]
    length = br2int(data[p+1:p+5])
    p += 5
    if status == 2:
        break
    elif status == 0:
        content = data[p:p+length]
        with file("img_%d.png"%count, "wb") as f:
            f.write(content)
            count += 1
        p += length
    elif status == 1:
        print "Removed!"
        p += length
    else:
        print "ERROR"
        break
    print count

