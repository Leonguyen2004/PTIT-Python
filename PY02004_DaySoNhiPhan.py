n = int(input())
List = [int(i) for i in input().split()]
cnt = 0
for i in range(1,n):
    if List[i] != List[i-1]:
        cnt += 1
print(cnt)