import math

def solve(s):
    n = int(s[-4:])
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return "NO"
    if n > 1:
        return "YES"
    else:
        return "NO"

def main():
    for _ in range(int(input())):
        s = input()
        print(solve(s))

if __name__ == "__main__":
    main()