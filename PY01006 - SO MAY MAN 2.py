def solve(myList):
    for i in myList:
        if i != 4 and i != 7:
            return False
    return True

for _ in range(int(input())):
    myList = [int(i) for i in input()]
    if solve(myList):
        print("YES")
    else:
        print("NO")