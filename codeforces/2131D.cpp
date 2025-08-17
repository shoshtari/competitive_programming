#include <bits/stdc++.h>
using namespace std;

void op() {
	int n;
	cin >> n;
	vector<int> deg(n, 0);
	map<int, set<int>> mp;
	for(int i = 0; i < n - 1; i++) {
		int u, v;
		cin >> u >> v;
		u--; v--;
		deg[u]++;
		deg[v]++;
		mp[u].insert(v);
		mp[v].insert(u);
	}
	int leaf_count = 0;
	for(int i = 0; i < n; i++) {
		if (deg[i] == 1) {
			leaf_count++;
		}
		mp[i].insert(i); // Include the node itself in the set
	}

	int best = -1;
	for(int i = 0; i < n; i++) {
		int cost = leaf_count;
		for (auto j : mp[i]) {
			if (deg[j] == 1) {
				cost--;
			}
		}
		if (cost < best || best == -1) {
			best = cost;
		}
	}
	cout << best << endl;


}
int main(){
	int t;
	cin >> t;
	for(int i = 0; i<t; i++){
		op();
	}
}

