#include <iostream>
#include <array>
#include <algorithm>

/**
 * Mutate «current» into next combination
 * Returns false if provided current state is a last combination
 */
template <int N, int K>
bool next_combination(std::array<int, K> &current, int min = 1) {
  auto head = current.begin();
  auto tail = current.end();

  auto max = min + N - 1;

  // current combination is last: {max-K+1, max-K, ..., max-1, max}
  if ((*head) == max - K + 1) return false;

  auto it = tail;
  for (--it; *it == max - (tail-it) + 1; --it);
  (*it)++;
  while (++it != tail) *it = *(it-1) + 1;

  return true;
}


/**
 * Traverses all (9, N) permutations and prints all solution, if found
 */
template <int N>
void solve(int (*get_solution)(const std::array<int, N>), int no_solution)
{
  std::array<int, N> digits;
  // Set initial combination: 1, 2, 3, ..., N
  for (int i = 0; i < N; ++i) digits[i] = i + 1;
  do {
    std::array<int, N> vars(digits);
    do {
      int solution = get_solution(vars);
      if (solution != no_solution) {
        std::cout << solution << "\n";
      }
    } while (std::next_permutation(vars.begin(), vars.end()));
  } while(next_combination<9, N>(digits));
}

constexpr bool CALC = true;

int main()
{
  if (CALC) {
    const int no_solution = -1;
    solve<3>([](const std::array<int, 3> args) -> int {
      int a = args[0];
      int b = args[1];
      int g = args[2];

      int d = (b * g) % 10;
      if (d == a || d == b || d == g) return no_solution;

      int v = (10 + d*g - b) % 10;
      if (v == a || v == b || v == g || v == d) return no_solution;

      int ab  =  10 * a + b;
      int vg  =  10 * v + g;
      int ddd = 111 * d;
      int vv  =  11 * v;

      return (ab * vg == ddd) && (d * vg - ab == vv) ? ab*g : no_solution;
    }, no_solution);
  } else {
    std::cout << "74\n";
  }
}
