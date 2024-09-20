import math

def cmp(s):
    res = 1
    for i in s:
        res *= int(i)
    return (res, int(s))

def solve():
    n = int(input())
    a = input().split()
    a.sort(key = cmp)
    print(*a)

def main():
    for _ in range(int(input())):
        solve()

if __name__ == "__main__":
    main()