n = int(input())
a = [float(i) for i in input().split()]
ma = max(a)
mi = min(a)
rl = []
for i in a:
    if i != mi and i != ma:
        rl.append(i)
print("{:.2f}".format(sum(rl) / len(rl)))