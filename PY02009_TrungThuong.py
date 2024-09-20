import math

def solve():
    mTuple = {}
    MAX = 0
    res = 1001
    n = int(input())
    for i in range(n):
        x = int(input())
        if x in mTuple:
            mTuple[x] += 1
        else:
            mTuple[x] = 1
        MAX = max(MAX, mTuple[x])
    for i in mTuple:
        if mTuple[i] == MAX:
            res = min(res, i)
    print(res)
        
def main():
    for _ in range(int(input())):
        solve()

if __name__ == "__main__":
    main()