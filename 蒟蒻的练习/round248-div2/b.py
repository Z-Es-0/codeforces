#1是前缀和
#2是
n=int(input())
s=list(map(int,input().split()))
su=0
sunn=[0]
for i in s:
    su+=i
    sunn.append(su)
g=sorted(s)
op=0
suu=[0]
for q in g:
    op+=q
    suu.append(op)
for _ in range(int(input())):
    type, l, r = map(int, input().split())
    if type == 1:
        print(sunn[r] - sunn[l - 1])
    else:
        print(suu[r]-suu[l-1])