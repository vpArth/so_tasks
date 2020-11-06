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
    printf("%" PRIu64 "\n", solve(118051));                  // 1
    printf("%" PRIu64 "\n", solve(118051ULL*11));            // 118051
    printf("%" PRIu64 "\n", solve(118051ULL*118051));        // 118051
    printf("%" PRIu64 "\n", solve(-1ULL));                   // 6148914691236517205
    printf("%" PRIu64 "\n", solve(18446744065119617025ULL)); // 6148914688373205675 // (IMAX - 1)**2
    printf("%" PRIu64 "\n", solve(18446744030759878681ULL)); // 4294967291 // max64(prime**2)
    printf("%" PRIu64 "\n", solve(18446744073709551557ULL)); // max64(prime), 14sec
}
