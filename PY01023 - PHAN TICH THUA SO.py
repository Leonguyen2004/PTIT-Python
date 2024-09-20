import math

for _ in range(int(input())):
    n = int(input())
    res = "1"
    for i in range(2, int(math.sqrt(n))+1):
        cnt = 0
        while n % i == 0:
            n /= i
            cnt += 1
        if cnt != 0:
            res += " * " + str(i) + "^" + str(cnt)
    if n != 1:
        res += " * " + str(int(n)) + "^1"
    print(res)
