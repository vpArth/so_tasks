#include <cstring>
#include <algorithm>

class LongNum {
    bool neg;
    char* np;
    int len;
    char sum_digits(const char a, const char b, char &carry) {
        auto s = a - '0' + b - '0' + carry;

        carry = s / 10;
        s = s % 10;

        return s + '0';
    }
    char sub_digits(const char a, const char b, char &carry) {
        auto s = (a - '0') - (b - '0') - carry;
        carry = s < 0;
        s = (s + 10) % 10;

        return s + '0';
    }

public:
    LongNum(char* num) {
        neg = num[0] == '-';
        np = num;
        len = std::strlen(num);
        if (neg) {
            np++; // skip sign
            len--;
        }
    }

    void add(LongNum b, char* result) {
        char carry = 0;
        int i = len - 1, j = b.len - 1, ri = 0;

        while (i >= 0 && j >= 0) result[ri++] = sum_digits(np[i--], b.np[j--], carry);
        while (i >= 0)           result[ri++] = sum_digits(np[i--], '0', carry);
        while (j >= 0)           result[ri++] = sum_digits('0', b.np[j--], carry);
        if (carry) {
            result[ri++] = sum_digits('0', '0', carry);
        }

        result[ri] = '\0';
        std::reverse(result, result+ri);
    }
    void sub(LongNum b, char* result) {
        char carry = 0;
        int i = len - 1, j = b.len - 1, ri = 0;

        while (i >= 0 && j >= 0) result[ri++] = sub_digits(np[i--], b.np[j--], carry);
        while (i >= 0)           result[ri++] = sub_digits(np[i--], '0', carry);
        while (j >= 0)           result[ri++] = sub_digits('0', b.np[j--], carry);
        if (carry) {
            result[ri++] = sub_digits('0', '0', carry);
        }

        result[ri] = '\0';
        std::reverse(result, result+ri);
    }

    int cmp(LongNum b) {
        if (len > b.len) return 1;
        if (len < b.len) return -1;
        for (int i = 0; i < len;) {
            if (np[i] > b.np[i]) return 1;
            if (np[i] < b.np[i]) return -1;
        }
        return 0;
    }
};

const int MAX_LEN = 100;
#include <iostream>
int main() {
    using namespace std;

    char a_buff[MAX_LEN+2] = "25";
    char b_buff[MAX_LEN+2] = "999";
    char c_buff[MAX_LEN+3];
    LongNum a{a_buff};
    LongNum b{b_buff};

    a.add(b, c_buff);
    cout << a_buff << " + " << b_buff << " = " << c_buff << endl;

    b.sub(a, c_buff);
    cout << b_buff << " - " << a_buff << " = " << c_buff << endl;

    a.sub(b, c_buff);
    cout << a_buff << " - " << b_buff << " = " << c_buff << endl;
}
