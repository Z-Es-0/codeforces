t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort(reverse=True)
    di=0
    for i in range(n):
        di+=max(abs(a[i]-b[i]),abs(a[i-n]-b[i-n]))
    print(di)