#include <algorithm>
#include <cmath>
#include <execution>
#include <iostream>
#include <utility>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <unordered_map>

using namespace std;

void dfs(int n, int cur, map<int, vector<int>>& children, vector<int>& dp, vector<bool>& done, string s){
	int ans = 0;
	for(auto c: children[cur]){
		if (!done[c]){
			dfs(n, c, children, dp, done, s);
		}
		ans+= dp[c];
	}
	if (s[cur] == 'B'){
		ans++;
	} else{
		ans--;
	}
	dp[cur] = ans;
	done[cur] = true;
}

void solve() {
	int n;
	cin >> n;
	map<int, vector<int>> children;
	for(int i = 1; i<n; i++){
		int parent;
		cin >> parent;
		parent--;
		children[parent].push_back(i);
	}
	string colors;
	cin >> colors;
	vector<int> dp(n);
	vector<bool> done(n, false);
	dfs(n, 0, children, dp, done, colors);
	int ans = 0;
	for(int i = 0; i<n; i++){
		if (dp[i] == 0){
			ans++;
		}
	}
	cout << ans << endl;
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    solve();
  }
}

