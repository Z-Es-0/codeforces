for _ in range(int(input())):
    s=input()
    n=len(s)
    for i in range(n):
        for j in range(i+1,n):
            if(int(s[i]+s[j])%25==0):
                a=n-i-2
    print(a)