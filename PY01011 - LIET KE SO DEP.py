def isValid(num):
    if len(num) % 2 == 1 or num != num[::-1]:
        return False
    for i in num:
        if int(i) % 2 == 1:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    for num in range(22, n, 2):
        if(isValid(str(num))):
           print(num, end=" ")
    print()