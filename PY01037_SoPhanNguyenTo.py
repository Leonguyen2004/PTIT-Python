def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count

def generate_unprime(limit): 
    unPrime = []
    maxDivisor = 0
    for i in range(1, limit):
        iDivisor = count_divisors(i)
        if iDivisor > maxDivisor:
            maxDivisor = iDivisor
            unPrime.append(i)
    return unPrime

def main():
    LIMIT = int(10**6) + 5
    unPrime = generate_unprime(LIMIT)

    for _ in range(int(input())):
        n = int(input())
        for p in unPrime:
            if p >= n:
                print(p)
                break

if __name__ == "__main__":
    main()
