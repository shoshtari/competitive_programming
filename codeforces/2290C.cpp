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
	int n;
	cin >> n;
	vector<int> h(n);
	for(int i = 0; i<n; i++){
		cin >> h[i];
	}
	sort(h.begin(), h.end());
	vector<int> l, r;
	l.push_back(h[0]);
	bool twice = false;
	int penalty = 0;
	for(int i = 1; i<n; i++){
		if (h[i] != h[i - 1]){
			l.push_back(h[i]);
			twice = false;
			continue;
		}
		if (!twice){
			r.push_back(h[i]);
			twice = true;
			continue;
		}
		l.push_back(h[i]);
		penalty++;
	}
	cout << l.size() + r.size() - penalty << endl;
	for(int i = 0; i<l.size(); i++){
		cout << l[i] << " ";
	}
	for(int i = r.size() - 1; i>=0; i--){
		cout << r[i] << " ";
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

