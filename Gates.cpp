// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;

#define ARR_SIZE 4003
bool visited[ARR_SIZE][ARR_SIZE];
bool fences[ARR_SIZE][ARR_SIZE];

int minx = ARR_SIZE-1;
int miny = ARR_SIZE-1;
int maxx = 0;
int maxy = 0;

void floodfill(int x, int y) {
    stack<pair<int, int>> s;
    s.emplace(x, y);
    while (!s.empty()) {
        auto [nx, ny] = s.top();
        s.pop();
        if (visited[nx][ny] || fences[nx][ny] || nx < minx || ny < miny || nx > maxx || ny > maxy) {
            continue;
        }
        visited[nx][ny] = true;
        s.emplace(nx + 1, ny);
        s.emplace(nx - 1, ny);
        s.emplace(nx, ny + 1);
        s.emplace(nx, ny - 1);
    }
}

int main() {
    freopen("gates.in", "r", stdin);
    freopen("gates.out", "w", stdout);

    cin.tie(nullptr);
    ios_base::sync_with_stdio(false);

    int n; cin >> n;
    string directions; cin >> directions;

    int x = 2001;
    int y = 2001;

    for (char& d : directions) {
        int dx = 0;
        int dy = 0;
        if (d == 'N') dy = 1;
        if (d == 'S') dy = -1;
        if (d == 'W') dx = -1;
        if (d == 'E') dx = 1;

        x += dx;
        y += dy;
        fences[x][y] = true;
        x += dx;
        y += dy;
        fences[x][y] = true;

        minx = min(minx, x);
        miny = min(miny, y);
        maxx = max(maxx, x);
        maxy = max(maxy, y);
    }

    if (minx > 0) minx--;
    if (miny > 0) miny--;
    if (maxx < ARR_SIZE-1) maxx++;
    if (maxy < ARR_SIZE-1) maxy++;

    int regions = 0;
    for (int i = minx; i < maxx; i++) {
        for (int j = miny; j < maxy; j++) {
            if (!visited[i][j] && !fences[i][j]) {
                floodfill(i, j);
                regions++;
            }
        }
    }
    cout << regions - 1 << endl;
}
