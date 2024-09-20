import math

def solve():
    s = input()
    n = input()
    l = len(n)
    id = s.find(n)
    cnt = 0
    while id != -1:
        cnt += 1
        id = s.find(n, id+l)
    print(cnt)

def main():
    for _ in range(int(input())):
        solve()

if __name__ == "__main__":
    main()  