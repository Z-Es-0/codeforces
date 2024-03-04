for _ in range(int(input())):
    n = int(input())
    a =list(map(int, input().split()))
    t1, t2 =1000005,1000005
    an = 0
    for i in range(n):
        if t1 > t2:
            t1, t2 = t2, t1
        if a[i] <= t1:
            t1 = a[i]
        elif a[i] <= t2:
            t2 = a[i]
        else:
            t1 = a[i]
            an += 1
    print(an)