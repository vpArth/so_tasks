#include <string>
#include <iostream>
#include <algorithm>
#include <climits>

unsigned int reverse1(unsigned int n) {

    auto n1 = n;
    auto num_width = 0;
    while (n1) {
        num_width++;
        n1 >>= 1;
    }

    unsigned res = 0;
    unsigned current_pow = 1 << (num_width-1);
    while (n) {
        if (n & 1) {
            res += current_pow;
        }

        current_pow >>= 1;
        n >>= 1;
    }

    return res;
}
unsigned reverse(unsigned n) {
    unsigned r = 0;
    for (r=n&1; n>>=1; r+=r+(n&1));
    return r;
}

#include <cmath>
unsigned reverse_harry(unsigned x)
{
    unsigned s=8*sizeof(x)-ceil(log2(x+(x&(x-1)==0)));

    x = (x & 0x55555555) << 1 | (x >> 1) & 0x55555555;
    x = (x & 0x33333333) << 2 | (x >> 2) & 0x33333333;
    x = (x & 0x0f0f0f0f) << 4 | (x >> 4) & 0x0f0f0f0f;
    x = (x << 24) | ((x & 0xFF00) << 8) | (( x >> 8) & 0xFF00) | (x >> 24);
    return s ? x >> s : x;
}
// int_bin = reverse(a);


int main()
{
   unsigned int int_bin, min= INT_MAX, max= 0;
   std::string result, binary, reverse_binary;
   int a,b;
     // cout << "enter segment[a:b]\n";
     a = 1; //cin >> a;
     b = 10000000; //cin >> b;
    auto b_width = 0;
    auto bt = b;
    while (bt) {
        b_width++;
        bt >>= 1;
    }


     if (a > max && b <= min && b >= 0 && a<=b) {
         for (; a <= b; a++) {
             int_bin = reverse(a);

             if (int_bin > max)
                 max = int_bin;

             if (int_bin < min&&min!=1)
                 min = int_bin;

         }
         std::cout << min << std::endl;
         std::cout << max << std::endl;
     }
     else
         std::cout << "Wrong input";

    std::cout << reverse(23) << std::endl;
   return 0;
}
