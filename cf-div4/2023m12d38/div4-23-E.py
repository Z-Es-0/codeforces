t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    asum, bsum = 0, 0
    h = set()
    iop = False

    for i in range(n):
        if (i + 1) % 2 == 0:
            bsum += a[i]
        else:
            asum += a[i]
        diff = asum - bsum
        if diff == 0 or diff in h:
            is_found = True
            break
        else:
            h.add(diff)
    if not iop:
        print("NO")
    else:
        print("YES")