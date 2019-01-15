# coding: utf-8

from bitstring import BitStream

s = BitStream(filename="t.bmp")
s.pos = 0x436*8

while s.pos <= s.len-7:
    s.insert('0b0', s.pos)
    s.pos += 7

f = file('gen.bmp', 'wb')
s.tofile(f)
f.close()
print 'Done'
