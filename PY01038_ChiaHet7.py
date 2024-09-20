import math

def solve(n):
    for i in range(1000):
        if n % 7 == 0: return n
        reverN = int(str(n)[::-1]) 
        n += reverN
    return -1

def main():
    for _ in range(int(input())):
        n = int(input())
        print(solve(n))

if __name__ == "__main__":
    main()