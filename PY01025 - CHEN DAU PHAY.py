num = input()
for i in range(len(num)-3, 0, -3):
    num = num[:i] + "," + num[i:]
print(num)