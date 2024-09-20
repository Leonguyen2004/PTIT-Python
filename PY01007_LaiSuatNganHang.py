import math

for _ in range(int(input())):
    n, x, m = (float(i) for i in input().split())
    # m = n*(1+x%)^res
    res = math.log(m / n, 1 + x/100)
    print(math.ceil(res))