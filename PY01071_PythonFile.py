import math



def main():
    s = input().lower()
    if len(s) >= 3 and s[-3:] == ".py":
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    main()