import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return n > 1

def solve(s):
    sum = 0
    for i in s:
        sum += int(i)
    if isPrime(sum): return "YES"
    return "NO"

def main():
    for _ in range(int(input())):
        s = input()
        print(solve(s))

if __name__ == "__main__":
    main()