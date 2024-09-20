from math import log2

BASE = '0123456789ABCDEF' #chuyen doi giua cac he co so

testCase = int(input())
while testCase > 0:
    testCase -= 1

    #input
    base = int(log2(int(input()))) 
    num = input() #chuoi nhi phan
    
    #them so 0 vao de tao thanh cac nhom co base phan tu
    while len(num) % base != 0:
        num = '0' + num 
    
    #tao mang mu cua 2 theo chieu nguoc 
    pow2 = [1]
    for i in range(1,base):
        pow2 = [pow2[0]*2] + pow2 

    #chuyen doi co so
    res = ""
    for i in range(0, len(num), base):
        tmp = 0
        for j in range(i, i+base):
            tmp += int(num[j]) * pow2[j-i]
        res += BASE[tmp]
    
    #output
    print(res)