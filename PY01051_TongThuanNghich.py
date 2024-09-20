import math

def solve(s):
    sum = 0
    for i in range(0, len(s)):
        sum += int(s[i])
    res = str(sum)
    if len(res) > 1 and res == res[::-1]:
        return "YES"
    return "NO"

def main():
    for _ in range(int(input())):
        s = input()
        print(solve(s))

if __name__ == "__main__":
    main()