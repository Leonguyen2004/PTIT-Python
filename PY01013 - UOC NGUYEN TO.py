import math

def isPrime(num):
    for i in range(2, int(math.sqrt(num)) +1):
        if num % i == 0:
            return False
    return num > 1

for _ in range(int(input())):
    a,b = [int(i) for i in input().split()]
    c = str(math.gcd(a,b))
    res = 0
    for i in c:
        res += int(i)
    if(isPrime(res)):
        print("YES")
    else:
        print("NO")
    