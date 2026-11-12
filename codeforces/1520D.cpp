#include <algorithm>
#include <cmath>
#include <iostream>
#include <map>
#include <queue>
#include <stack>
#include <unordered_map>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
void solve() {
  ll n;
  cin >> n;
  ll a[n];
	map<ll, ll> groups;
  for (ll i = 0; i < n; i++) {
		ll tmp;
		cin >> tmp;
		tmp -= i;
		if (groups.find(tmp) == groups.end()){
			groups[tmp] = 0;
		}
		groups[tmp]++;
  }
	ll ans = 0;
	for(auto u: groups){
		ll count = u.second;
		if (count < 2){
			continue;
		}
		ans += count * (count - 1) / 2;

	}
	cout << ans << endl;

}

int main() {
  ll t;
  cin >> t;
  for (ll i = 0; i < t; i++) {
    solve();
  }
}
