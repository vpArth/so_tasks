#include <iostream>
#include <tuple>

#define CALC 0

void solve(bool (*check)(int, int, int, int, int))
{
  using std::cout;
  for (int a = 1; a < 10; a++)
  for (int b = 1; b < 10; b++) if (b != a)
  for (int g = 1; g < 10; g++) if (g != a && g != b)
  {
    int d = (b * g) % 10;         if (d == a || d == b || d == g) continue;
    int v = (100 + d*g - b) % 10; if (v == a || v == b || v == g || v == d) continue;

    if (check(a, b, v, g, d)) {
      cout << (10*a+b) * g << "\n";
    }
  }
}

int main()
{
#ifdef CALC
  solve([](int a, int b, int v, int g, int d) -> bool {
    int ab  =  10 * a + b;
    int vg  =  10 * v + g;
    int ddd = 111 * d;
    int vv  =  11 * v;

    return (ab * vg == ddd) && (d * vg - ab == vv);
  });
#else
  std::cout << "74\n";
#endif
}
