#include <cinttypes>
#include <cstdio>
#include <climits>
#include <vector>
#define IMAX 4294967296ULL // (1ULL<<32) == sqrt(UINT64_MAX)

void gen_primes() {
    std::vector<uint64_t> primes;
    uint64_t num;

    num = 2;
    primes.push_back(num);

    num = 3;

    while (num < IMAX) {
        bool is_prime = true;
        for (auto p: primes) {
            if (p * p > num) break;
            if ((num % p == 0)) {
                is_prime = false;
                break;
            }
        }
        if (is_prime) {
            primes.push_back(num);

            if ((primes.size() + 1) % 10000 == 0) {
                printf("%" PRIu64 "^2 = %" PRIu64 "\n", num, num*num);
            }
        }
        num += 2;
    }
    auto m = primes[primes.size()-1];
    printf("%" PRIu64 "^2 = %" PRIu64 "\n", m, m*m);
}

int main()
{
    gen_primes();

    return 0;
}
