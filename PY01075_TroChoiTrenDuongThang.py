import math

def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]

    INF = float("inf")
    minCost = INF

    for i in range(0, (1 << n)):
        gcd_value = 0
        cost = 0
        for j in range(n):
            if i & (1 << j):
                gcd_value = math.gcd(gcd_value, a[j])
                cost += c[j]

        if gcd_value == 1:
            minCost = min(minCost, cost)

    if minCost != INF:
        print(minCost)
    else:
        print(-1)


def main():
    for _ in range(int(input())):
        solve()

if __name__ == "__main__":
    main()