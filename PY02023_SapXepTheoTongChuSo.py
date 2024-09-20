import math

def solve():
    n = int(input())
    a = input().split()
    a.sort(key=lambda s: (sum(int(i) for i in s), int(s)))
    print(*a)

def main():
    for _ in range(int(input())):
        solve()

if __name__ == "__main__":
    main()