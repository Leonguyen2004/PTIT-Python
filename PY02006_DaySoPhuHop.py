import math

def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a.sort()
    b.sort()
    for i in range(n):
        if a[i] > b[i]:
            return "NO"
    return "YES"

def main():
    for _ in range(int(input())):
        print(solve())

if __name__ == "__main__":
    main()