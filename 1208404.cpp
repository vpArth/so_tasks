unsigned solve(unsigned n) {
  int zeroes = 0;
  unsigned result = 0;
  while (n) {
      // Считаем единицы и нули
      if (n&1) result = (result << 1) | 1; // вдвигаем единицы
      else zeroes++;
      n >>= 1;
  }
  result <<= zeroes; // Вдвигаем нули

  return result;
}


#include <bit>
#include <concepts>

template <std::unsigned_integral T>
T tsolve(const T& n, bool full_width = true) {
    if (n == -1u || n == 0) {
        return n;
    }

    T t (~T{});
    T shift = (T)(sizeof(T)*8 - std::popcount(n));

    if (full_width) {
        return t << shift;
    }

    t >>= shift;
    t <<= shift - std::countl_zero(n);

    return t;
}

#include <iostream>
int main() {
    std::cout << solve(1024) << std::endl; // 1024
    std::cout << solve(1025) << std::endl; // 1536 = 2^10+2^9
    // 10000000001 -> 11000000000
    std::cout << solve(682) << std::endl; // 992
    // 1010101010 -> 1111100000
    std::cout << solve(-1u) << std::endl; // 4294967295
    std::cout << solve(0) << std::endl; // 0


    std::cout.setf(std::ios::hex, std::ios::basefield);
    std::cout << tsolve(uint32_t(1033)) << std::endl;          // e0000000
    std::cout << tsolve(uint16_t(1033)) << std::endl;          // e000

    std::cout << tsolve(uint32_t(1033), false) << std::endl;   // 700
}

