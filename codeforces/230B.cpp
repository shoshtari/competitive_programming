#include <algorithm>
#include <cmath>
#include <iostream>
#include <utility>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <unordered_set>
#include <unordered_map>

using namespace std;


typedef long long ll;
unordered_set<ll> sieve(){
	ll maxp = 1e6 + 10;
	unordered_set<ll> primes;
	unordered_set<ll> notprimes;
	primes.insert(4);
	primes.insert(9);

	for (ll i = 6; i < maxp; i+=6){
		ll a = i - 1;
		ll b = i + 1;

		if (notprimes.find(a) == notprimes.end()){
			primes.insert(a * a);
			for (ll j = a * a; j < maxp; j += a){
				notprimes.insert(j);
			}
		}
		if (notprimes.find(b) == notprimes.end()){
			primes.insert(b * b);
			for (ll j = b * b; j < maxp; j += b){
				notprimes.insert(j);
			}
		}
	}
	return primes;

}

int main() {
  long long t;
  cin >> t;
  unordered_set<ll> primes = sieve();
  for (long long i = 0; i < t; i++) {
	  ll n;
	  cin >> n;
	  if (primes.find(n) != primes.end()){
		  cout << "YES" << endl;
	  }
	  else{
		  cout << "NO" << endl;
	  }
  }
}
