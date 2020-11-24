#include <iostream>

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
      arr[i+1] = (arr[i] + arr[i+1]) % MOD;
    }
    // std::cout << r+1 << ": "; print(arr, n, "\t");
  }
}

void solve_mul(int* arr, const int n, int k) {
    for (auto i = 1; i < n; ++i) {
      arr[i] = (int)((long long)arr[i-1]*k + arr[i]) % MOD;
    }
}

void solve_sqr(int* arr, const int n, int k) {
  // fixme: Точность всё ещё теряется, не пойму где =)
    for (int i = 1; i < n; ++i) {
      unsigned long long term = k;
      auto sign = 1;
      for (int j = 1; j <= i; ++j) {
        if (sign == 1) {
          arr[i] =  (int)((long)(arr[i] + sign * (unsigned long long)(term % MOD * arr[i-j] % MOD)) % MOD);
        } else {
          arr[i] =  (int)((long)(arr[i] + sign * (unsigned long long)(term * arr[i-j])) % MOD);
        }
        term = (term * (k-j) / (j+1)) ;
        sign = -sign;
        while (arr[i] < 0) {
          arr[i] = arr[i] + MOD;
        }
      }
    }
}

void debug(int k, int n, int start, int mult) {
  int *arr = new int[n];
  int *A = new int[n];
  for (int i = 0, d=start; i < n; ++i, d*=mult) {
    arr[i] = d;
    A[i] = d;
  }
  solve(arr, n, k);
  solve_sqr(A, n, k);
  print(arr, n);
  print(A, n);

  delete[] arr;
  delete[] A;
}

int main() {
  int start = 5;
  for (int k = 64; k <= 68; ++k) {
    std::cout << "\nk = " << k << "; start=" << start << std::endl;
    debug(k, 25, start, 5);
  }

  const int n = 20;
  int k = 100;

  int arr0[]{5, 25, 125, 625, 13, 17, 19, 23, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
  solve(arr0, n, k);
  print(arr0, n);
  // 3 5266946 586395883 760641300 100716517 676709075 11153447 256148068 149906432 237819898 589215151 630658815 656728361 66027592 551072302 318065800 839518503 598503241 909406756 741324981

  int arr[]{5, 25, 125, 625, 13, 17, 19, 23, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
  solve_sqr(arr, n, k);
  print(arr, n);
}
/*
12: 1 13 91 458 1856 6422 19656 54483 139074 331058 742118 1578824 3208036 6258448 11773996 21440094 37910187 65268135 109671705 180234210

a[k, r] = a[k, r-1] + a[k-1, r]
a[k, r] = a[k, r-1] + a[k-2, r] + a[k, r-1] - a[k, r-2]
a[k, r] = 2*a[k, r-1] - a[k, r-2] + a[k-2, r]

a[k, 0] = a[0, 0]
a[k, 1] = a[k, 0] * k + a[0, 1]
a[k, 2] = a[k, 1] * k - a[k, 0]*(k-1) + a[0, 2]



*/
