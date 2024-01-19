from math import gcd

for _ in range(int(input())):
    x = int(input())
    l = list(map(int, input().split()))
    p = -1
    d = {}#打表，寻找对应值的最大索引。
    for i in range(x):
        d[l[i]] = i + 1#更新最大索引
    for i in d:
        for j in d:
            if d[i] + d[j] > p and gcd(i, j) == 1:#更新最大值
                p = d[i] + d[j]
    print(p)