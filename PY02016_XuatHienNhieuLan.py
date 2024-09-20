import math

def solve():
    n = int(input())
    a = [int(i) for i in input().split()]

    dd = {}
    Max = 0
    res = int(1e7)
    for i in a:
        if i in dd:
            dd[i] += 1
        else:
            dd[i] = 1
        Max = max(Max, dd[i])
    for i in dd:
        if dd[i] == Max:
            res = min(res, i)
    if dd[res] * 2 > len(a):
        print(res)
    else:
        print("NO")
    


def main():
    for _ in range(int(input())):
        solve()

if __name__ == "__main__":
    main()