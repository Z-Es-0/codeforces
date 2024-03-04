for _ in range(int(input())):
    n=int(input())
    s=list(input())
    f=list(input())
    a=0;b=0
    for i in range(n):
        if s[i]=='1' and f[i]=='0':
            a+=1
        if s[i]=='0' and f[i]=='1':
            b+=1
    print(max(a,b))