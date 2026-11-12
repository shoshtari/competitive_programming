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
	string s;
	cin >> s;
	int ans = 0;
	if (s[0] == 'B'){
		ans++;
	}
	for(int i = 1; i<n; i++){
		if (s[i] == s[i - 1]){
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

