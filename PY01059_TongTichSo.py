import math

def solve():
    n = input()
    sum = 0
    mul = 1
    flag = False
    for i in range(0, len(n), 2):
        if int(n[i]) != 0:
            mul *= int(n[i])
            flag = True
    if flag == False:
        print(0, end = " ")
    else:
        print(mul, end = " ")
    
    for i in range(1, len(n), 2):
        sum += int(n[i])
    print(sum)
    

def main():
    for _ in range(int(input())):
        solve()

if __name__ == "__main__":
    main()