import math

n, k = (int(i) for i in input().split())
a = 10 ** (k-1)
b = 10 ** k
cnt = 0
for i in range(a, b):
    if math.gcd(n, i) == 1:
        print(i, end=" ")
        cnt += 1
        if cnt % 10 == 0:
            print()
    