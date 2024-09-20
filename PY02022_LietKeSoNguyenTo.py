import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

n = int(input())
a = [int(i) for i in input().split()]
res = {}
for i in a:
    if isPrime(i):
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
for i in res:
    print(i, res[i])