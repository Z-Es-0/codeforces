#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;

    vector<int> a(n);
    for (int &i : a)
        cin >> i;

    int ans = 0;
    for (int k = 1; k <= n; k++) {
        if (n % k == 0) {
            int g = 0;
            for (int i = 0; i < n - k; i++)
                g = gcd(g, abs(a[i + k] - a[i]));
            ans += g != 1;
        }
    }
    cout << ans << "\n";
}

int main() {

    int t;
    cin >> t;
    while (t--)
        solve();
}