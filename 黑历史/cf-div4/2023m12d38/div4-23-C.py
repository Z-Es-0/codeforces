import math
for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    p=sum(s)
    if int(math.sqrt(p))*int(math.sqrt(p))==p:
        print('YES')
    else:
        print('NO')