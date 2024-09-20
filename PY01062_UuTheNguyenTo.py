import math

def isPrime(n):
    #if n == 0: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: 
            return False
    return n > 1

def solve(n):
    if not isPrime(len(n)):
        return False
    
    cnt = 0
    for i in n:
        if isPrime(int(i)):
            cnt += 1
    
    if cnt > len(n) - cnt:
        return True
    return False

def main():
    for _ in range(int(input())):
        n = input()
        if solve(n):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()