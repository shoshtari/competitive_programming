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
  // cout << "########################\n";
  int n;
  cin >> n;
  string s;
  cin >> s;
  int l = -1;
  int r = -1;
  vector<pair<int, int>> points;
  for (int i = 0; i < n / 2; i++) {
    char c1 = s[i], c2 = s[n - i - 1];
    if (c1 == c2) {
      continue;
    }
    if (c1 > c2) {
      c1 ^= c2 ^= c1 ^= c2;
    }
    // c1, c2
    // cout << "R " << c1 + 1 - 'a' << " " << c2 - 'a' << endl;
    points.push_back({c2 - 'a', 1});
    points.push_back({c1 + 1 - 'a', 0});
  }
  if (points.size() == 0) {
    cout << 0 << endl;
    return;
  }
  sort(points.begin(), points.end());
  int last = 0;
  int cur = 0;
  int ans = 26;
  for (auto p : points) {
    // cout << p.first << " " << p.second << endl;
    if (cur == 0 && p.first > last) {
			// cout << "REF " << p.first - last << endl;
      ans -= p.first - last;
    }
    last = p.first + 1;
    if (p.second == 0) {
      cur++;
    } else {
      cur--;
    }
  }
  int ind = points.size() - 1;
  ans -= 'z' - 'a' - points[ind].first;
			// cout << "REF " <<  'z' - 'a' - points[ind].first << endl;
  cout << ans << endl;
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    solve();
  }
}
