for _ in range(int(input())):
    exp = input()
    res = ""
    for i in range(0,len(exp),2):
        res += exp[i]*int(exp[i+1])
    print(res)