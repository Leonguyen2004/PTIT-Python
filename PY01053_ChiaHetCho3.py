import math

def solve(s):
    if(s % 3 == 0): print("YES")
    else: print("NO")

def main():
    for _ in range(int(input())):
        s = int(input())
        solve(s)

if __name__ == "__main__":
    main()