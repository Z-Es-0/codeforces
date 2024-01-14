def solve():
    n, k, x = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + sorted(A, reverse=True)
 
    for i in range(1, n + 1):
        A[i] += A[i - 1]
 
    ans = -1e9
    for i in range(k + 1):
        ans = max(ans, A[n] - 2 * A[min(i + x, n)] + A[i])
 
    print(ans)
 
tc = int(input())
for _ in range(tc):
    solve()