import math

def solve(n):
    if len(n) % 2 == 0:
        return False
    if n[0] == n[1]:
        return False
    for i in range(2, len(n), 2):
        if n[i] != n[0]:
            return False
    return True

def main():
    for _ in range(int(input())):
        n = input()
        if solve(n):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()