n = int(input())
List = [int(i) for i in input().split()]
cnt = 0
for i in range(0, n-1):
    for j in range(i+1, n):
        if List[i] > List[j]: cnt += 1
print(cnt)