import math

def solve(n):
    for i in range(2, len(n)):
        if n[i] != n[i-2]: return "NO"
    return "YES"

def main():
    for _ in range(int(input())):
        n = input()
        print(solve(n))

if __name__ == "__main__":
    main()