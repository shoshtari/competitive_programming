#include <algorithm>
#include <cmath>
#include <iostream>
#include <utility>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <unordered_map>

using namespace std;

typedef long long ll;
void solve() {
	ll n, k;
	cin >> n >> k;
	vector<ll> a(n);
	for(ll i = 0; i<n; i++){
		cin >> a[i];
	}
	map<ll, ll> carryt;
	ll carry = 0;
	ll total = 0;
	// cout << "##################################\n";

	for(ll i = n - 1; i>=0; i--){
		// cout << i << " " << a[i] << " " << carry << endl;
		total += a[i] + carry;
		// this pile
		ll t = i - k;
		if (t < 0){
			t = 0;
		}
		if (carryt.find(t) == carryt.end()){
			carryt[t] = 0;
		}
		carryt[t] += a[i] + carry;
		carry += a[i] + carry;

		// terminate
		if (carryt.find(i) != carryt.end()){
			carry -= carryt[i];

		}
	}
	// cout << total << endl;
	if ((total & 1) == 1){
		cout << "Alice\n";
	} else{
		cout << "Bob\n";
	}


}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    solve();
  }
}

