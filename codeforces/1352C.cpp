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

void solve() {
	int n, k;
	cin >> n >> k;
	int rem = 0;
	if (n == 2){
		cout << 2 * (k - 1) + 1 << endl;
		return;

	}
	if (k % (n - 1) == 0){
		k++;
		rem+=2;
	}
	int ans = k % (n - 1);
	// cout << "N: " << n << " K: " << k << " r: " << rem << endl;
	ans = (k - ans) / (n - 1) * n + ans;
	ans -= rem;
	cout << ans << endl;
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    solve();
  }
}

