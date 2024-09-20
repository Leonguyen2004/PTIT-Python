import math

def solveThapHN(n, fromRod, toRod, auxRod):
    if n == 1:
        print(f"{fromRod} -> {toRod}")
        return
    
    solveThapHN(n-1, fromRod, auxRod, toRod)
    print(f"{fromRod} -> {toRod}")
    solveThapHN(n-1, auxRod, toRod, fromRod)

def main():
    n = int(input())
    solveThapHN(n, 'A', 'C', 'B')

if __name__ == "__main__":
    main()