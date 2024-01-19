import math as gcd
def main():
    n=int(input())
    s=list(map(int,input().split()))
    s.sort(reverse=True)

    for i in range(n):
        t=False
        for j in range(1,n):
            if gcd(s[i],s[j])==1:
                print(i+j)
                t=True
                break
        if t:
            break

for _ in range(int(input())):
    main()