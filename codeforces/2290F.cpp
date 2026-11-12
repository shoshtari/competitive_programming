#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

void solve() {
	int n;
	cin >> n;
	vector<int> b(n);
	for(int i = 0; i<n; i++){
		cin >> b[i];
	}
	// tree<pair<int, int>, null_type, less<pair<int, int>>, rb_tree_tag, tree_order_statistics_node_update> c;
	// c.insert({n + b[0] - 1, 1});
	// cout << "I " << n + b[0] - 1 << " " << 0 << endl;

	// for(int i = 1; i<n; i++){
	// 	int l= 0, r = i - 1;
	// 	while (r> l){
	// 		int minim = (l + r) / 2;
	// 		// int val = c.find_by_order(minim)->second;

	// 		if (b[minim] <= b[i]){
	// 			r = minim - 1;
	// 		} else {
	// 			l = minim + 1;
	// 		}

	// 	}
	// 	int ind = b[i] + l - (i - l) + n;
	// 	cout << "I " << ind << " "  << l << " " << endl;
	// 	c.insert({ind, i + 1});
	// }
	// cout << "##############\n";
	vector<int> ans(n, 0);
	for(int i = 0; i<n; i++){
		int ind = n - i + b[i] - 1;
		// cout << "A " << ind << endl;
		if(ind < 0 || ind >= n || ans[ind] != 0){
			cout << -1 << endl;
			return;
		}
		ans[ind] = i + 1;
		// if (ans[u.first] != 0){
		// 	cout << -1 << endl;
		// 	return;
		// }
		// ans[u.first] = u.second;

	}
	for(auto u: ans){
		cout << u << " ";
	}
	cout << endl;
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    solve();
  }
}

