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
ll max(ll a, ll b){
	return a > b ? a : b;
}
ll min(ll a, ll b){
	return a < b ? a : b;
}

void solve() {
	ll n, k;
	cin >> n >> k;
	vector<ll> a(n);
	for (ll i = 0; i < n; i++) {
		cin >> a[i];
		}
	vector<ll> b(n);
	for (ll i = 0; i < n; i++) {
		cin >> b[i];
		}
	vector<pair<ll, ll>> c;
	map<pair<ll, ll>, ll> cCount;
	for (ll i = 0; i < n; i++) {
		pair<ll, ll> u;
		u = make_pair(a[i], 0);
		if (cCount.find(u) == cCount.end()){
			cCount[u] = 1;
			c.push_back(u);
		} else {
			cCount[u] += 1;
		}

		u = make_pair(b[i], 1);
		if (cCount.find(u) == cCount.end()){
			cCount[u] = 1;
			c.push_back(u);
		} else {
			cCount[u] += 1;
		}
	}
	sort(c.begin(), c.end());
	ll neg = 0;
	ll best = -1;
	ll count = n;

	for(ll i = 0; i < c.size(); i++){
		pair<ll, ll> u = c[i];
		if (u.second == 0){ // it is a
			if (neg <= k){
				ll earn = u.first * count;
				best = max(best, earn);
			}
			neg += cCount[u];
		} else { // it is b
			if (neg <= k){
				ll earn = u.first * count;
				best = max(best, earn);
			}
			count -= cCount[u];
			neg -= cCount[u];
		}
	}
	cout << best << "\n";
}

int main() {
  long long t;
  cin >> t;
  for (long long i = 0; i < t; i++) {
    solve();
  }
}
