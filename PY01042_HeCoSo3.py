import math

def solve(num):
    for i in num:
        if i < '0' or i > '2':
            return "NO"
    return "YES"

def main():
    for _ in range(int(input())):
        num = input()
        print(solve(num))

if __name__ == "__main__":
    main()