#include <iostream>
using namespace std;

int main() {
    // input
    string S;
    cin >> S;

    // solve & output
    if (S[0] == S[1] || S[1] == S[2] || S[2] == S[3]) {
        cout << "Bad" << endl;
    } else {
        cout << "Good" << endl;
    }

    return 0;
}
