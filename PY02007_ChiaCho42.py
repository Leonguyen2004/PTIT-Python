import math

dd = [0] * 42
cnt =  10
while cnt > 0:
    a = [int(i) for i in input().split()]
    cnt -= len(a)
    for i in a:
        dd[i % 42] += 1

res = 0
for i in dd:
    if i > 0:
        res += 1
print(res)