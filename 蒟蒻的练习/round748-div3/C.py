t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    x = list(map(int, input().split()))
    x.sort(reverse=True)

    cnt = 0
    su = 0

    while cnt < len(x) and su + n - x[cnt] < n:
        su += n - x[cnt]
        cnt += 1
    print(cnt)