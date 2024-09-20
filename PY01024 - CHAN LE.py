def check(num):
    sum = 0
    for i in num:
        sum += int(i)
    if sum % 10 != 0: 
        return "NO"
    for i in range(0, len(num)-1):
        if abs(int(num[i]) - int(num[i+1])) != 2:
            return "NO"
    return "YES"

for _ in range(int(input())):
    num = input()
    print(check(num))
    