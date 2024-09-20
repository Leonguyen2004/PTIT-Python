# num = input()
# flag = 1
# for i in range(len(num)):
#     if not num[i].isdigit():
#         flag = 0
# if (flag == 1):
#     number = int(num)
#     if number%2 == 0:
#         print("CHAN")
#     else:
#         print("LE") 
# else:
#     print("Invalid")

s = input()
try:
    n = int(float(s)) 
except ValueError:
    print("invalid:", end = " ")
    number = s
    for i in range(len(number)):
        if not number[i].isdigit():
            print(i, end = " ")
else:
    if n%2 == 0:
        print("CHAN")
    else:
        print("LE")




