#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <unordered_map>

using namespace std;

typedef long long ll;

set<ll> sieve(ll n){
	set<ll> primes;
	set<ll> complexes;
	for (ll i = 2; i  < n; i++){
		if (complexes.find(i) == complexes.end()){
			primes.insert(i);
			for (ll j = i * i; j <= n; j += i){
				complexes.insert(j);
			}
		}
	}
	return primes;
}

void solve() {
	ll n;
	cin >> n;
	vector<ll> a(n);
	ll maxa = 0;
	set<ll> unique;
	for (ll i = 0; i < n; i++) {
		cin >> a[i];
		unique.insert(a[i]);
	}

	if (unique.size() < n) {
		cout << "NO" << endl;
		return;
	}
	set<ll> primes = sieve(n / 2 + 1);
	map<ll, set<ll>> mp;

	for (ll i = 0; i < n; i++) {
		ll x = a[i];
		for (ll p : primes) {
			if (mp[p].find(x % p) != mp[p].end()){
				mp[p].insert(p + x % p);
			} else{
				mp[p].insert(x % p);
			}

			if (mp[p].size() >= 2 * p) {
				cout << "NO" <<  endl;
				return;
			}
		}
	}
	cout << "YES" << endl;

}

int main() {
  ll t;
  cin >> t;
  for (ll i = 0; i < t; i++) {
    solve();
  }


}

