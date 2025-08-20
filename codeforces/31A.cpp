#include <bits/stdc++.h>
using namespace std;


int main(){
	int n;
	cin >> n;
	vector<int> a(n);
	for(int i = 0; i < n; i++) {
		cin >> a[i];
	}

	for(int i = 0; i < n; i++) {
		map<int, int> rem;
		for(int j = 0; j < n; j++) {
			if(i == j) continue;
			int needed = a[i] - a[j];
			if (rem.find(needed) != rem.end()) {
				cout << i + 1 << " " << j + 1 << " " << rem[needed] + 1 << endl;
				return 0;
			}
			rem[a[j]] = j;
		}
	}
	cout << -1 << endl;

	return 0;
}
