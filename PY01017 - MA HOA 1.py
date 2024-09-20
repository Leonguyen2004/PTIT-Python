for _ in range(int(input())):
    exp = input() + "!"
    res = ""
    cnt = 0
    i = 0
    while i < len(exp) - 1:
        cnt = 1
        j = i + 1
        while exp[j] == exp[i]:
            j += 1
            cnt += 1
        res += str(cnt) + exp[i]
        i += cnt
    print(res)
