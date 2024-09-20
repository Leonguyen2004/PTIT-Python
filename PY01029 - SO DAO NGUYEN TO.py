import math

def check(num):
    a = int(num)
    b = int(num[::-1])
    c = math.gcd(a,b)
    if c != 1: return "NO"
    return "YES"

for _ in range(int(input())):
    num = input()
    print(check(num))