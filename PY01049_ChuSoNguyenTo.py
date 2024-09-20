import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return n>1

def solve(s):
    if not isPrime(len(s)): return False
    cnt = 0
    for i in s:
        if isPrime(int(i)): cnt += 1
    return cnt > len(s) - cnt

def main():
    for _ in range(int(input())):
        s = input()
        if solve(s): print("YES")
        else: print("NO")

if __name__ == "__main__":
    main()