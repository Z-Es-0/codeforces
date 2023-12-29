def split_string(s, i):
    r = []
    p = 0
    for x in i:
        r.append(s[p:x])
        p = x
    r.append(s[p:])
    return '.'.join(r)
v={'a','e'}
c={'b','c','d'}
for _ in range(int(input())):
    a=int(input())
    s=input()
    g=[]
 
    for i in range(0,a-1):
        if (s[i] in c)and (s[i+1] in c):
            g.append(i+1)
        if (s[i]in c) and (s[i+1] in v) and (s[i-1] in v):
            g.append(i)
    if split_string(s,g)[0]=='.':
        print(split_string(s,g)[1::])
    else:
        print(split_string(s,g))