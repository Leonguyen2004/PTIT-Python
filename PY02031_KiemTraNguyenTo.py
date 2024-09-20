import math

def standard(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return int(n > 1)

n, m = [int(i) for i in input().split()]
for i in range(n):
    List = [standard(int(j)) for j in input().split()]
    print(*List)