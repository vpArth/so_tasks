#include <inttypes.h>
#define IMAX 4294967296ULL // (1ULL<<32) == sqrt(UINT64_MAX)

uint64_t solve(uint64_t n) {
  if ((n & 1) == 0) return n >> 1;
  uint64_t i = 3;

  while (i < IMAX && i*i <= n) {
    if (n % i == 0)
      return n / i;
    i += 2;
  }
  return 1;
}


#include <stdio.h>
#include <limits.h>
int main()
{
    printf("%" PRIu64 "\n", solve(118051));               // 1
    printf("%" PRIu64 "\n", solve(118051ULL*11));          // 118051
    printf("%" PRIu64 "\n", solve(118051ULL*118051));      // 118051
    printf("%" PRIu64 "\n", solve(IMAX*IMAX - 1));
    printf("%" PRIu64 "\n", solve(UINT64_MAX));
    printf("%" PRIu64 "\n", solve(18446744073709551557ULL)); // max prime, 14sec
}
