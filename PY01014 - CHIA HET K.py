# a, k, n = (int(i) for i in input().split())

# bmin = (int(a/k) + 1) * k - a
# bmax = int(n/k) * k - a
# if bmin < bmax and bmin > 0 and bmax > 0:
#     for i in range(bmin, bmax+1, k):
#         print(i, end=" ")
# else:
#     print(-1)

s = input().split()
try:
    a = int(s[0])
except:
    print("Nhap sai kieu du lieu")

