#So nguyen to cung nhau
import math

def isprime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return n > 1

for _ in range(int(input())):
    n = int(input())
    k = 0
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            k += 1
    if isprime(k):
        print("YES")
    else:
        print("NO")
    