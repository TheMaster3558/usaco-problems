// TLE on last test case

#include <bits/stdc++.h>
using namespace std;

int main() {
	int x, n; cin >> x >> n;

	multiset<int> distances;
	distances.insert(x);

	set<int> lights;


	for (int i = 0; i < n; i++) {
		int p; cin >> p;
		int left = 0;
		int right = x;

		lights.insert(p);
		auto it = lights.find(p);

		auto rightIt = it;
		if (++rightIt != lights.end()) {
			right = *rightIt;
		}

		auto leftIt = it;
		if (leftIt != lights.begin() && --leftIt != lights.end()) {
			left = *leftIt;
		}


		distances.erase(distances.find(right - left));
		distances.insert(right - p);
		distances.insert(p - left);
		cout << *distances.rbegin() << " ";
	}
}
