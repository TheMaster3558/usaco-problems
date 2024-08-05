// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;


void splitSet(const std::set<int>& originalSet, std::set<int>& smallestHalf, std::set<int>& largestHalf) {
    int n = 0;
    for (auto& i : originalSet) {
        if (n++ < originalSet.size()/2) {
            smallestHalf.insert(i);
        }
        else {
            largestHalf.insert(i);
        }
    }
}

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);
    freopen("cardgame.in", "r", stdin);
    freopen("cardgame.out", "w", stdout);

    int n; cin >> n;
    vector<int> elsie(n);
    set<int> elsie_has;
    for (int i = 0; i < n; i++) {
        cin >> elsie[i];
        elsie_has.insert(elsie[i]);
    }

    set<int> bessie;
    for (int i = 1; i < n*2+1; i++) {
        if (elsie_has.find(i) == elsie_has.end()) {
            bessie.insert(i);
        }
    }

    set<int> smaller;
    set<int> bigger;
    splitSet(bessie, smaller, bigger);

    int s = 0;
    for (int i = 0; i < n / 2; i++) {
       auto it = bigger.upper_bound(elsie[i]);
       if (it == bigger.end()) {
           bigger.erase(bigger.begin());
       }
       else {
           bigger.erase(it);
           s++;
       }
    }
    for (int i = n/2; i < n; i++) {
        auto it = smaller.lower_bound(elsie[i]);
       if (it == smaller.begin()) {
           smaller.erase(--smaller.end());
       }
       else {
           it--;
           smaller.erase(it);
           s++;
       }
    }
    cout << s << endl;

}
