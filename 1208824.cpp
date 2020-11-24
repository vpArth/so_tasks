#include <iostream>
#include <cstdint>

const auto MOD = 998244353;

void print(int* arr, const int n, const char *glue=" ") {
  for (auto i = 0; i < n; ++i) {
    if (i) std::cout << glue;
    std::cout << arr[i];
  }
  std::cout << std::endl;
}

void solve(int* arr, const int n, int k) {
  for (auto r = 0; r < k; ++r) {
    for (auto i = 0; i < n-1; ++i) {
      arr[i+1] = (int)((arr[i] + arr[i+1]) % MOD);
    }
  }
}
int64_t gcd_ex(uint64_t a, uint64_t b, int64_t &x, int64_t &y) {
  if (a == 0) {
    x = 0; y = 1;
    return b;
  }
  int64_t x1, y1, t;
  int64_t d = gcd_ex((b+a) % a, a, x1, y1);
  t = (b / a) * x1;
  x = y1 - t;
  y = x1;

  return d;
}

uint64_t reciprocal_mod(uint64_t a, uint64_t m) { // a**-1 (mod m)
  int64_t x{}, y{};
  if (gcd_ex(a, m, x, y) == 1) {

    return x < 0 ? x + m : x;
  }
  std::cerr << a << " and " << m << " are coprimes\n";
  return 1; // no reciprocal
}

void solve_sqr(int* arr, const int n, int k) {
    // A_k_i = A_0_i + \sum_{j=1}^i -1^{j-1}* \frac{k!}{j!(k-j)!}*A_0_{(i-j)}
    for (int i = 1; i < n; ++i) {
      uint64_t term = k;
      auto sign = 1;
      for (int j = 1; j <= i; ++j) {
        // arr[i] += sign * term * arr[i-j];
        // term = term * (k-j) / (j+1);
        uint64_t t = term;
        t = (t * sign) % MOD;
        t = (t * arr[i-j]) % MOD;
        arr[i] = (int)((arr[i] + t) % MOD);

        term = (term * (k-j)) % MOD;
        term = (term * reciprocal_mod(j+1, MOD)) % MOD;

        sign = (sign == 1) ? MOD - 1 : 1;
      }
    }
}

void test_reciprocal_mod() {
  if(reciprocal_mod(2, 27) != 14) {
    std::cerr << "[FAIL] reciprocal_mod(2) is "<< reciprocal_mod(2, 27) <<", 14 expected" << std::endl;
  }
  if(reciprocal_mod(2, MOD) != 499122177) {
    std::cerr << "[FAIL] reciprocal_mod(2) is "<< reciprocal_mod(2, MOD) <<", 499122177 expected" << std::endl;
  }
  if(reciprocal_mod(7, MOD) != 855638017) {
    std::cerr << "[FAIL] reciprocal_mod(7) is "<< reciprocal_mod(2, MOD) <<", 855638017 expected" << std::endl;
  }
  if(reciprocal_mod(18, MOD) != 720954255) {
    std::cerr << "[FAIL] reciprocal_mod(18) is "<< reciprocal_mod(2, MOD) <<", 720954255 expected" << std::endl;
  }
  for (int i = 2; i < 10000; ++i) {
    auto rec = reciprocal_mod(i, MOD);
    auto res = ((uint64_t)rec * i) % MOD;
    if (res != 1) {
      std::cerr << "[FAIL] reciprocal_mod(" << i << ") * "<<i<<" = " << rec << "*"<<i<<"(mod M)="<< (rec*i)%MOD <<  ", 1 expected" << std::endl;
    }
  }
}

void test_solve(void (*fn)(int*, const int, int), int n, int k, int start, int mult, int expected) {
    int *A = new int[n];
    for (int i = 0, d=start; i < n; ++i, d=(int)(((uint64_t)d*mult) % MOD)) {
      A[i] = d;
    }
    fn(A, n, k);
    if (A[n-1] != expected) {
      std::cerr << "Last element is " << A[n-1] << "; " << expected << " expected\n";
    }
    delete[] A;
}

int main() {
  test_reciprocal_mod();
  test_solve(solve, 100, 1e6, 1, 1, 428943052);
  test_solve(solve_sqr, 100, 1e6, 1, 1, 428943052);
  test_solve(solve_sqr, 2000, 1e9, 13, 7, 92923453);
  test_solve(solve_sqr, 2000, 1e9, 1, 1, 93451579);
  test_solve(solve_sqr, 2000, 1e9, 2, 1, 186903158);
}
