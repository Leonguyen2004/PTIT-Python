n = int(input())
mat = [[]] * n
for i in range(n):
    mat[i] = [int(j) for j in input().split()]
k = int(input())

sumUp, sumDow = 0, 0
for i in range(n):
    for j in range(n):
        if i < j:
            sumDow += mat[i][j]
        elif i > j:
            sumUp += mat[i][j]

sub = abs(sumUp - sumDow)
if sub <= k:
    print("YES")
else:
    print("NO")
print(sub)