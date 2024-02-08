for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    ls=s[0]
    for i in range(n):
        if s[i]!=ls:
            ans=i
            break
    if s[1]==s[2] and s[0]!=s[1]:

        print(1)
    else:
        print(ans+1)