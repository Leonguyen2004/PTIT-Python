import math

def solve(n):
    if len(n) % 2 == 1 or n != n[::-1]:
        return False
    for i in n:
        if int(i) % 2 == 1:
            return False
    return True


def main():
    for _ in range(int(input())):
        num = int(input())
        for i in range(22, num, 2):
            if solve(str(i)):
                print(i, end=' ')
        print()

if __name__ == "__main__":
    main()