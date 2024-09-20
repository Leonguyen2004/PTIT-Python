tc = int(input())
while tc > 0:
    tc-=1
    s = input()
    s += 'z'
    ans = 10 ** 20
    x = 0
    for i in range(len(s)):
        if s[i].isdigit():
            x = x*10 + int(s[i])
        else:
            if i != 0 and s[i-1].isdigit():
                ans = min(ans,x)
                x = 0
    print(ans)
        
