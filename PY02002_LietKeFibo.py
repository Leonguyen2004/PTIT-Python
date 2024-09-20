import math

fb = [1] * 93
def prepare():
    for i in range(3, 93):
        fb[i] = fb[i-1] + fb[i-2]

def solve():
    a,b = [int(i) for i in input().split()]
    for i in range(a, b+1):
        print(fb[i], end = " ")
    print()

def main():
    prepare()
    for _ in range(int(input())):
        solve()

if __name__ == "__main__":
    main()