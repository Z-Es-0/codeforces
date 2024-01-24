def cal(a, b, c):
   
    va = max(0, max(b, c) - a + 1)
    vb = max(0, max(a, c) - b + 1)
    vc = max(0, max(a, b) - c + 1)

    return va, vb, vc
t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    result = cal(a, b, c)

    print(*result)