t = int(input())


for _ in range(t):
    g = [0] * 26
    p = [chr(ord('A') + i) for i in range(26)]
    o = 0
    n = int(input())
    log = input()
    for i in log:
        g[p.index(i)]+=1
    for q in range(26):
        if g[q]>=q+1:
            o+=1

    print(o)




