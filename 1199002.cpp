#include <iostream>
#include <string>
using namespace std;


auto solve(string input) {
    auto res = 1Lu;
    for (char ch: input) {
        if ((ch < '0') or ('9' < ch)) {
            throw invalid_argument( "Incorrect number" );
        }
        res *= ch - '0';
    }

    return res;
}

int main() {

    string number;

    cin >> number;
    while (number != "0") {
        try {
            cout << solve(number) << endl;
        } catch (const invalid_argument& e) {
            cout << e.what() << endl;
        }
        cin >> number;
    };


    return 0;
}
