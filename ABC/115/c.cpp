#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define endl "\n"

const int INF = 1000000000;

int main() {
    int N, K;
    cin >> N >> K;
    vector<ll> h(N);
    for (int i = 0; i < N; ++i) {
        cin >> h[i];
    }

    sort(h.begin(), h.end());
    ll ans = INF;
    for (int i = 0; i < N - K + 1; ++i) {
        ans = min(ans, h[i + K - 1] - h[i]);
    }

    cout << ans << endl;
    return 0;
}
