def solve(num):
    for i in range(0, len(num)-1):
        if num[i] > num[i+1]:
            return "NO"
    return "YES"

for _ in range(int(input())):
    num = input()
    print(solve(num))
    