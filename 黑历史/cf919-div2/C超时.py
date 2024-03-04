import math
def main():
    n = int(input())
    a=list(map(int,input().split()))
    ans = 0
    for k in range(1, n + 1):
        if n % k == 0:
            g = 0
            for i in range(n - k):
                g = math.gcd(g, abs(a[i + k] - a[i]))
            ans += g != 1
    print(ans)
for _ in range(int(input())):
    main()