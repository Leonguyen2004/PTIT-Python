import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return n>1

def solve(n):
    for i in range(0, len(n)):
        if not (isPrime(i) ^ isPrime(int(n[i]))):
            continue
        else:
            return "NO"
    return "YES"

def main():
    for _ in range(int(input())):
        n = input()
        print(solve(n))

if __name__ == "__main__":
    main()