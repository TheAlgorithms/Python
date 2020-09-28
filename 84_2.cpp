#include <bits/stdc++.h>
#define int long long 
#define pb push_back
#define fr first
#define sc second
#define mp make_pair
#define all(a) a.begin(),a.end()
#define rep(i,a,n) for(int i=a;i<n;i++)
#define N 7200001
#define M 1000000007
using namespace std;
signed main(){
ios::sync_with_stdio(0);
cin.tie(0);
int t;
cin>>t;
while(t--){
  int n,un=0;
  cin>>n;
  vector<int>v(n);
  rep(i,0,n) v[i]=0;
  rep(i,0,n){
    int k;
    cin>>k;
    int a=1;
    rep(j,0,k){
      int pr;
      cin>>pr;
      if(!v[pr-1]&&a){v[pr-1]=1;a=0;}
    }
    if(a==1) un = i+1;
  }
  if(un==0) cout<<"OPTIMAL"<<endl;
  else {
    cout<<"IMPROVE"<<endl;
    cout<<un<<" ";
    rep(i,0,n){if(v[i]==0){cout<<i+1<<endl;break;}}
  }

}
}