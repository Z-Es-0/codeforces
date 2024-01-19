'''计算数组 a
 的前缀和：让 bi=a1+⋯+ai
 问题重述：对于每个包含整数 k
 的问题，我们需要找到最大的 ai
 使得 a1,…,ai
 都最多是 k
 然后输出 bi换句话说
 就是 max(a1,…,ai)≤k
 我们来做数组的前缀最大值：设为 mi=max(a1,…,ai)
 然后，我们需要找到 i
 中最大的 mi≤k
 这可以通过二进制搜索来实现，因为数组 m
 是不递减的。找到索引 i
 后，我们只需输出 bi'''

import bisect
for _ in range(int(input())):
    n,q=map(int,input().split())
    s=list(map(int,input().split()))
    g=list(map(int,input().split()))
    an=[]
    su = 0
    b = [0]
    ma=0
    for i in s:#双重测试问题拆开想，将一部分做成有序然后二分可以大大降低复杂度。
        if i>ma:
            ma=i
        su += i
        b.append(su)
        an.append(ma)
    for w in g:
        p=bisect.bisect(an,w)
        print(b[p],end=' ')
    print()

