#include<bits/stdc++.h>
using namespace std;
int a[1000],b[1000];
void solve(){
    int mx=0;
    int n,m;
    cin>>n>>m;
    for (int i=1;i<=n;i++)cin>>a[i];
    for (int i=1;i<=n;i++)cin>>b[i];
    int sum=0;
    int ans=0;
    for (int i=1;i<=min(n,m);i++){
        sum+=a[i];
        mx=max(mx,b[i]);
        ans=max(ans,sum+(m-i)*mx);
    }
    cout<<ans<<endl;

}
int main(){
    int t;
    cin>>t;
    while (t--)solve();
    return 0;
}
