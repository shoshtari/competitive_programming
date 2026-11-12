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
  // cout << "EEEEEEEEEEEEEEEEEE\n";
  ll n, l, r;
  cin >> n >> l >> r;
  vector<ll> a(n);
  for (ll i = 0; i < n; i++) {
    cin >> a[i];
  }
  sort(a.begin(), a.end());
  ll ans = 0;
  for (ll i = 0; i < n; i++) {
    auto l1 = lower_bound(a.begin(), a.end(), l - a[i]);
    auto l2 = upper_bound(a.begin(), a.end(), r - a[i]);
    ll pairs = l2 - l1;
		if (l <= a[i] + a[i] && a[i] * 2  <= r){
			pairs--;
		}
    // cout << a[i] << " " << pairs << endl;

    if (pairs > 0) {
      ans += pairs;
    }
  }
  cout << ans / 2 << endl;
}

int main() {
  ll t;
  cin >> t;
  for (ll i = 0; i < t; i++) {
    solve();
  }
}
