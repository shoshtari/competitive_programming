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
	int n, c;
	cin >> n >> c;
	vector<int> a(n);
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	sort(a.begin(), a.end());

	int k = 1;
	int saved = 0;
	for(int i = n - 1; i >= 0; i--) {
		if (a[i] * k <= c){
			saved ++;
			k *= 2;
		}
	}
	cout << n - saved << endl;

}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    solve();
  }
}

