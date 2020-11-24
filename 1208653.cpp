#include <iostream>
#include <vector>

using namespace std;

class Solution {
    vector<int> col;
    vector<int> diag1;
    vector<int> diag2;
    int N;
    int ans = 0;

public:
    Solution() =delete;
    Solution(int n) {
        N = n;
        col.resize(n);
        diag1.resize(2*n-1);
        diag2.resize(2*n-1);

        solve();
    }
    ~Solution() {
    }
    int count() {
        return ans;
    }
private:

    void solve(int y = 0) {
        if (y == N) {
            ans++;
            return;
        }
        for (int x = 0; x < N; x++) {
            if (col[x] || diag1[x + y] || diag2[x - y + N - 1]) continue;
            col[x] = diag1[x + y] = diag2[x - y + N - 1] = 1;
            solve(y + 1);
            col[x] = diag1[x + y] = diag2[x - y + N - 1] = 0;
        }
    }
};

int main() {
    for (int i = 1; i <= 16; ++i) {
        cout << i << ": " << (new Solution(i))->count() <<endl;
    }
}

