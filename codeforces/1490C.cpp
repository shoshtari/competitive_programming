#include <algorithm>
#include <cmath>


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
bool iscube(ll n){
	double val2 = pow(n, 1.0/3.0);
	ll val = (ll) val2;
	if (val * val *val == n){
		return true;
	}
	val++;
	if (val * val *val == n){
		return true;
	}
	return false;

}

void solve() {
	ll x ;
	cin >> x;
	for(ll i = 1; i * i * i < x; i++){
		if (iscube(x - i * i * i)){
			cout << "YES\n";
			return;
		}
	}
	cout << "NO\n";
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    solve();
  }
}

