# coding: utf-8

ans = [[None]*8 for _ in range(8)]

def f(m, n):
    print m, n
    if m == 0:
        ans[m][n] = n+1
        return n+1

    if n == 0:
        if ans[m-1][1] is None:
            n = f(m-1, 1)
            ans[m-1][1] = n
            return n
        else:
            return ans[m-1][1]

    f_m_n_1 = ans[m][n-1]
    if f_m_n_1 is None:
        f_m_n_1 = f(m, n-1)
        if f_m_n_1 is None:
            print "Error!"
        ans[m][n-1] = f_m_n_1

    if ans[m-1][f_m_n_1] is not None:
        return ans[m-1][f_m_n_1]
    else:
        n = f(m-1, f_m_n_1)
        ans[m-1][f_m_n_1] = n
        return n

for i in range(7):
    for j in range(7):
        f(i, j)

print hex(f(7, 7))
