#include <iostream>
#include <cmath>
#include <set>
// #define NDEBUG
#include <cassert>
#include <limits>

using namespace std;

bool check3(const unsigned long long num) {
    unsigned long c = 1;
    while (c < num) c *= 3;
    return c == num;
}

static set<unsigned long long> power3{
    1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489,
    1162261467, 3486784401, 10460353203, 31381059609, 94143178827, 282429536481, 847288609443, 2541865828329, 7625597484987, 22876792454961,
    68630377364883, 205891132094649, 617673396283947, 1853020188851841, 5559060566555523, 16677181699666569, 50031545098999707, 150094635296999121,
    450283905890997363, 1350851717672992089, 4052555153018976267, 12157665459056928801u};

bool is_num_power_of_3(const unsigned long long num) {
    return power3.count(num);
}

auto LOG3 = 1.0986122886681096913952452369225257046474905578227494517346943336L;

long double diff_deg3(const unsigned long long num) {
    long double d = logl(num) / LOG3;


    return d - (int)d;
}

bool is_deg3(const unsigned long long num) {
    return diff_deg3(num) <= 3.46945e-18;
}

/**
 * Много ложноположительных срабатываний начиная с 450283905890997362
 */
bool is_pow3(const unsigned long long num) {
    long double d = logl(num) / logl(3);


    return d - (int) d < 3.46945e-18;
}

bool is_pow3_pow(const unsigned long long num) {
    int d = logl(num) / logl(3);


    return num == powl(3, d);
}



int main(int argc, char const *argv[])
{
    cout.precision(std::numeric_limits<long double>::max_digits10);

    auto testF = is_pow3_pow;

    auto cnt = 0;
    auto k = 20;
    for (auto i = 1; i < 1000000; ++i) {
        if (testF(i) != is_num_power_of_3(i)) {
            cout << ++cnt << ". " << i  << " " << (is_num_power_of_3(i) ? "FNEG" : "FPOS") <<  " diff is "  << diff_deg3(i) << endl;
        }
    }
    for (unsigned long long num: power3) {
        if (num < 1000000) continue;

        for(auto i = -k; i <= k; ++i) {
            auto n = num + i;
            if (testF(n) != is_num_power_of_3(n)) {
                cout << ++cnt << ". " << n  << " " << (is_num_power_of_3(n) ? "FNEG" : "FPOS") <<  " diff is "  << diff_deg3(n) << endl;
            }
        }
    }

    return 0;
}
