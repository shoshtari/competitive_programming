#include <bits/stdc++.h>
using namespace std;

void op() {
	int n, k;
	cin >> n >> k;
	vector<int> a(n);
	for(int i = 0; i < n; i++) {
		cin >> a[i];
	}
	vector<int> b(n);
	for(int i = 0; i < n; i++) {
		cin >> b[i];
	}
	map<int, int> s, t;
	for(int i = 0; i < n; i++) {
		a[i] %= k;
		int sk = a[i];
		if (k - sk < sk){
			sk = k - sk;
		}
		if (s.find(sk) == s.end()) {
			s[sk] = 0;
		}
		s[sk]++;

		b[i] %= k;
		int tk = b[i];
		if (k - tk < tk){
			tk = k - tk;
		}
		if (t.find(tk) == t.end()) {
			t[tk] = 0;
		}
		t[tk]++;
	}
	for (auto it = s.begin(); it != s.end(); it++) {
		if (t.find(it->first) == t.end() || t[it->first] != it->second) {
			cout << "NO" << endl;
			return;
		}
	}

	cout << "YES" << endl;

}
int main(){
	int t;
	cin >> t;
	for(int i = 0; i<t; i++){
		op();
	}
}

