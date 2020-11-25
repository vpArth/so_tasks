#include <iostream>
#include <array>
#include <algorithm>

/**
 * Mutate «current» into next combination
 * Returns false if provided current state is a last combination
 */
template <int N, int K>
bool next_combination(std::array<int, K> &current, const int min = 1) {
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
 * Traverses all (9, N) permutations and call the get_solution callback, if it returns true stops
 *
 * @param bool get_solution(array<int, N>) Should check is that int list a solution and do all things related to it(print, etc)
 *   - array is int list to prove
 *   - returns true, if solution found and no need other solutions
 */
template <int N>
void solve(bool (*get_solution)(const std::array<int, N>), const int start = 1)
{
  std::array<int, N> digits{};
  // Set initial combination: 1, 2, 3, ..., N
  for (int i = 0; i < N; ++i) digits[i] = i + start;
  do {
    std::array<int, N> vars = digits;

    do {
      if (get_solution(vars)) return; // Solution found, stop
    } while (std::next_permutation(vars.begin(), vars.end()));
  } while(next_combination<9, N>(digits, start));
}

constexpr bool CALC = false;

void puzzle_orig() {
  if (CALC) {
    solve<3>([](const std::array<int, 3> args) -> bool {
      int a = args[0];
      int b = args[1];
      int g = args[2];

      int d = (b * g) % 10;
      if (d == a || d == b || d == g) return false;

      int v = (10 + d*g - b) % 10;
      if (v == a || v == b || v == g || v == d) return false;

      int ab  =  10 * a + b;
      int vg  =  10 * v + g;
      int ddd = 111 * d;
      int vv  =  11 * v;

      if ((ab * vg == ddd) && (d * vg - ab == vv)) {
        std::cout << "\nSolution:\n";
        std::cout << "ab * vg = ddd:    " << ab << " * " << vg << " = " << ddd << std::endl;
        std::cout << "d * vg - ab = vv: " << d << " * " << vg << " - " << ab << " = " << vv << std::endl;
        std::cout << "ab * g = " << ab << " * " << g << " = " << ab*g << std::endl;
      };
      return false;
    });
  } else {
    std::cout << "\nSolution:\n"
                 "ab * vg = ddd:    37 * 12 = 444\n"
                 "d * vg - ab = vv: 4 * 12 - 37 = 11\n"
                 "ab * g = 37 * 2 = 74\n";
  }
}


void puzzle_draka() {
  if (CALC) {
    solve<5>([](const std::array<int, 5> args) -> bool {
      int u = args[0];
      int d = args[1];
      int a = args[2];
      int r = args[3];
      int k = args[4];

      int udar  = (((u*10 + d)*10 + a)*10 + r);
      int draka = (((d*10 + r)*10 + a)*10 + k)*10 + a;
      if (udar + udar == draka) {
        std::cout << "\nudar + udar = draka\n"
                  << udar << " + " << udar << " = " << draka << "\n";
      }
      return false;
    });
  } else {
    std::cout << "\nudar + udar = draka\n"
                 "8126 + 8126 = 16252\n";
  }
}

int main()
{
  puzzle_draka();
  puzzle_orig();
}
