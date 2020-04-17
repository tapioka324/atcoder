#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define endl "\n"

int main() {
    int N;
    string S;
    cin >> N >> S;

    vector<int> a(N);
    for (int i = 0; i < N; ++i) {
        if (S[i] == 'R') a[i] = 0;
        if (S[i] == 'G') a[i] = 1;
        if (S[i] == 'B') a[i] = 2;
    }
    vector<ll> cnt(3);
    for (int i = 0; i < N; ++i) {
        cnt[a[i]]++;
    }
    ll ans = 1;
    for (int i = 0; i < 3; ++i) {
        ans *= cnt[i];
    }
    for (int j = 0; j < N; ++j) {
        for (int i = 0; i < j; ++i) {
            int k = j + (j - i);
            if (k < N) {
                if (a[i] == a[j]) continue;
                if (a[i] == a[k]) continue;
                if (a[j] == a[k]) continue;
                ans--;
            }
        }
    }

    cout << ans << endl;
    return 0;
}
