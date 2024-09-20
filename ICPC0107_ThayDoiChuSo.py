for tc in range(int(input())):
    p, q = input().split()
    x1 = input()
    x2 = input()
    num1 = int(x1.replace(p,q)) + int(x2.replace(p,q))
    num2 = int(x1.replace(q,p)) + int(x2.replace(q,p))
    print(min(num1,num2), max(num1,num2))
