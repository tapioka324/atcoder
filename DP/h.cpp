#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define endl "\n"

const int MOD = 1000000007;

int main() {
    int H, W;
    cin >> H >> W;
    vector<string> a(H);
    for (int i = 0; i < H; ++i) {
        cin >> a[i];
    }

    vector<vector<int>> dp(H, vector<int>(W, 0));
    dp[0][0] = 1;

    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            dp[i][j] %= MOD;
            if (j + 1 < W && a[i][j + 1] == '.') {
                dp[i][j + 1] += dp[i][j];
            }
            if (i + 1 < H && a[i + 1][j] == '.') {
                dp[i + 1][j] += dp[i][j];
            }
        }
    }

    cout << dp[H - 1][W - 1] << endl;
    return 0;
}
