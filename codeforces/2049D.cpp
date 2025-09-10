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
void fill_dp(vector<vector<ll>> &dp, const vector<vector<ll>> &grid, ll n,
             ll m, ll row, ll k) {

  for (ll i = 0; i < m; i++) {
	vector<ll> dp2(m, 0);
	ll cost = k * i;
    for (ll j = 0; j < m; j++) {

      ll bestLast = -1;
      if (row > 0) {
        bestLast = dp[row - 1][j];
      }
      if (j > 0) {
		if (bestLast == -1) bestLast = dp2[j - 1];
        bestLast = min(bestLast, dp2[j - 1]);
      }
	  if (bestLast == -1) bestLast = 0;


      ll option = bestLast + grid[row][(i + j) % m];
	  dp2[j] = option;
	  option += cost;
	  if (dp[row][j] == -1 || option < dp[row][j]) {
		  dp[row][j] = option;
		  // cout << "FILL dp[" << row << "][" << j << "] = " << dp[row][j] << endl;
		  // cout << "cost: " << cost << " rotate: " << i << " grid: " << grid[row][(i + j) % m] << endl;
	  }
    }
  }
}
void solve() {
  ll n, m, k;
  cin >> n >> m >> k;
  vector<vector<ll>> grid(n, vector<ll>(m));
  for (ll i = 0; i < n; i++) {
    for (ll j = 0; j < m; j++) {
      cin >> grid[i][j];
    }
  }

  // cout << "#############\n";
  // for(ll i = 0; i < n; i++) {
	// for(ll j = 0; j < m; j++) {
		// cout << grid[i][j] << " ";
	// }
	// cout << endl;
  // }

  // cout << "#############\n";
  vector<vector<ll>> dp(n, vector<ll>(m, -1));
  for(ll i = 0; i < n; i++) {
	fill_dp(dp, grid, n, m, i, k);
	// for(ll j = 0; j < m; j++) {
	// 	cout << dp[i][j] << " ";
	// }
	// cout << endl;
  }
  // cout << "#############\n";
  // for(ll i = 0; i < n; i++) {
	// for(ll j = 0; j < m; j++) {
		// cout << dp[i][j] << " ";
	// }
	// cout << endl;
  // }

  cout << dp[n - 1][m - 1] << endl;
}

int main() {
  ll t;
  cin >> t;
  for (ll i = 0; i < t; i++) {
    solve();
  }
}
