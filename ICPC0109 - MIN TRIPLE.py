for _ in range(int(input())):
    n = int(input())

    min1,min2,min3 = float('inf'),float('inf'),float('inf')
    for _ in range(n):
            num = int(input())
            if num < min1:
                min3 = min2
                min2 = min1
                min1 = num
            elif num < min2:
                min3 = min2
                min2 = num
            elif num < min3:
                min3 = num

    print(min1 + min2 + min3)