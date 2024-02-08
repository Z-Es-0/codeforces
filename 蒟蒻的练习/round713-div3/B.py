def check(x,y,n):
    return x<n and y<n

if __name__ == '__main__':
    for _ in range(int(input())):
        g=[]
        u=[]
        n=int(input())
        for i in range(n):
            s=list(input())
            for j in range(n):
                if s[j]=='*':
                    g.append((i,j))
            u.append(s)
        if g[0][0]==g[1][0] :
            if g[0][0]+1<n:
                u[g[0][0]+1][g[0][1]]='*'
                u[g[1][0]+1][g[1][1]]='*'
            else:
                u[g[0][0]-1][g[0][1]] = '*'
                u[g[1][0]-1][g[1][1]] = '*'
        elif g[0][1]==g[1][1]:
            if g[0][1]+1<n:
                u[g[0][0]][g[0][1]+1]='*'
                u[g[1][0]][g[1][1]+1] = '*'
            else:
                u[g[0][0]][g[0][1] - 1] = '*'
                u[g[1][0]][g[1][1] - 1] = '*'
        else:
            r=max(g[0][1],g[1][1])
            t=min(g[0][0],g[1][0])
            u[t][r]='*'
            h=min(g[0][1],g[1][1])
            p=max(g[0][0],g[1][0])
            u[p][h]='*'
            r = max(g[0][1], g[1][1])
            t = max(g[0][0], g[1][0])
            u[t][r] = '*'
            h = min(g[0][1], g[1][1])
            p = min(g[0][0], g[1][0])
            u[p][h] = '*'
        for i in u:
            print(''.join(map(str,i)))