#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

// @unsolved for substraction

char sum_digits(char a, char b, char &carry) {
    auto s = a - '0' + b - '0' + carry;

    carry = s / 10;
    s = s % 10;

    return s + '0';
}


void summ(const char* a, const char* b, char* c) {
    auto a_len = strlen(a);
    auto b_len = strlen(b);

    bool a_neg = a[0] == '-';
    bool b_neg = b[0] == '-';

    if (a_len < b_len) {
        swap(a, b);
        swap(a_len, b_len);
    }

    char carry = 0;
    int i = a_len - 1, j = b_len - 1, ci = 0;
    while (i >= 0 && j >= 0) {
        c[ci++] = sum_digits(a[i], b[j], carry);
        --i; --j;
    }
    while(i >= 0) {
        c[ci++] = sum_digits(a[i], '0', carry);
        --i;
    }
    if (carry) {
        c[ci++] = carry + '0';
    }

    c[ci] = '\0';
    reverse(c, c+ci);
}

const int MAX_LEN = 100;
int main() {
    int T;
    char a[MAX_LEN+2];
    char b[MAX_LEN+2];
    char c[MAX_LEN+3];
    do {
        cout << "A: "; cin >> a;
        cout << "B: "; cin >> b;
        summ(a, b, c);
        cout << "A + B = " << c << endl;
        cout << "\nПродолжить - 1, закончить - 0." << endl;
        cin >> T;

    } while (T == 1);
}
