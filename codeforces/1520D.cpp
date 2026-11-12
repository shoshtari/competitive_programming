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

void solve() {
  int n;
  cin >> n;
  int a[n];
	map<int, int> groups;
  for (int i = 0; i < n; i++) {
		int tmp;
		cin >> tmp;
		tmp -= i;
		if (groups.find(tmp) == groups.end()){
			groups[tmp] = 0;
		}
		groups[tmp]++;
  }
	int ans = 0;
	for(auto u: groups){
		int count = u.second;
		if (count < 2){
			continue;
		}
		ans += count * (count - 1) / 2;

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
