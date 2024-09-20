import math

def solve():
    n = input()
    res = 1
    for i in n:
        if int(i) != 0:
            res *= int(i)
    print(res)

def main():
    for _ in range(int(input())):
        solve()

if __name__ == "__main__":
    main()