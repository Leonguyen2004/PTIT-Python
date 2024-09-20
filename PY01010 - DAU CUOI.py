for _ in range(int(input())):
    num = input()
    if num[0:2] == num[-2:]:
        print("YES")
    else:
        print("NO")