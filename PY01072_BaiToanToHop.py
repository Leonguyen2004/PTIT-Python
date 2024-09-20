def QLToHop(u):
    global k
    if u > k:
        for i in range(1, k+1):
            print(mlist[a[i]-1], end=" ")
        print()
        return
    for i in range(a[u-1]+1, l-k+u+1):
        a[u] = i
        QLToHop(u+1)


n,k = [int(i) for i in input().split()]
mlist = sorted(list({int(i) for i in input().split()}))
l = len(mlist)
a = [0] * 25
QLToHop(1)