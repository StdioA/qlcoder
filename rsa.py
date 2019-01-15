# coding: utf-8
# 使用 yafu 将 m 分解质因数

import sys

e = 65537
m = 41031587223377599579245988781518671358060455361860183212406274189493280555347897
f1 = 5991810554633396517767024967580894321153
f2 = 6847944682037444681162770672798288913849
phi_m = (f1-1)*(f2-1)
d = 9876455871473848869533324275271328267592369748302270589984220483284702063644673
code = 0x14a091645d307b8abd8632a1fb83f81e38c1b33d3286ca814a5742bec52c4b06d08

def calc(num, exp, mod):
    """快速幂"""
    if exp == 0:
        return 1
    elif exp == 1:
        return num%mod
    elif exp % 2 == 0:
        return (calc(num, exp/2, mod)**2)%mod
    else:
        return (calc(num, exp/2, mod)**2*num)%mod

# ans = hex(calc(code, d, m))[2:-1]
ans = hex(pow(code, d, m))[2:-1]
i = 0
while i < len(ans):
    sys.stdout.write(chr(int(ans[i:i+2], 16)))
    i += 2
