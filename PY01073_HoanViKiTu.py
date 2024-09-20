def QLHoanVi(res):
    global n, vs
    if len(res) == n:
        print(res)
        return
    for i in range(n):
        if vs[i] == 0:
            vs[i] = 1
            QLHoanVi(res + s[i])
            vs[i] = 0

s = input()
n = len(s)
vs = [0] * n
QLHoanVi("")