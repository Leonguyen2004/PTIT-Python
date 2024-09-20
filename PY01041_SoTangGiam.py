import math

def solve(num):
    if len(num) < 3: 
        return False
    
    peakFound = False
    for i in range(1, len(num)):
        if not peakFound:
            if num[i] > num[i-1]:
                continue
            elif num[i] < num[i-1]:
                peakFound = True
            else:
                return False
        else:
            if num[i] >= num[i-1]:
                return False
    return peakFound


def main():
    for _ in range(int(input())):
        num = input()
        if solve(num):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()