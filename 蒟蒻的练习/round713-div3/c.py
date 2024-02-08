def tian(s1,s2,a,b,n):
    for i in range(n//2):
        if s1[i]=='1' and s2[i]=='?':
            s2[i]='1'
            b-=2
        elif s1[i]=='0' and s2[i]=='?':
            s2[i]='0'
            a-=2
        elif s2[i]=='1' and s1[i]=='?':
            s1[i]='1'
            b-=2
        elif s2[i]=='0' and s1[i]=='?':
            s1[i]='0'
            a-=2
        else:
            if s1[i] == s2[i] == '1':
                b -= 2
            elif s1[i]==s2[i]=='0':
                a -= 2
    for i in range(n//2):
        if s1[i] == s2[i] == '?':
            if a > b:
                s1[i] = '0'
                s2[i] = '0'
                a -= 2
            else:
                s1[i] = '1'
                s2[i] = '1'
                b -= 2

    return a,b
if __name__ == '__main__':
    for _ in range(int(input())):
        a,b=map(int,input().split())
        s=list(input())
        n=len(s)
        # print(n)
        s1=s[:n//2]
        s2=s[n-n//2:]
        s3=s2[::-1]
        if n%2==0:
            a,b=tian(s1,s3,a,b,n)
            s1=''.join(s1)
            # print(s1)
            # print(a,b)
            s2=''.join(s1[::-1])
            if a!=0 or b!=0:
                print(-1)
            else:
                print(s1+s2)
        else:
            a, b = tian(s1, s3, a, b, n)
            zo=False
            s1 = ''.join(s1)
            s2 = ''.join(s1[::-1])

            if (n//2)<n and s[n//2]=='1':
                b-=1
                zo=True
            elif (n//2)<n and s[n//2]=='0':
                a-=1
                zo=True
            if zo and a==0 and b==0:
                print(s1+s[n//2]+s2)
            elif (not zo) and a==1 and b==0:
                print(s1+'0'+s2)
            elif (not zo) and a==0 and b==1:
                print(s1+'1'+s2)
            else:
                print(-1)
