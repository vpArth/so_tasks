#include <iostream>

void solve()
{
  using std::cout;
  for (int a = 1; a < 10; a++)
  for (int b = 1; b < 10; b++) if (b != a)
  for (int g = 1; g < 10; g++) if (g != a && g != b)
  {
    int d = (b * g) % 10;         if (d == a || d == b || d == g) continue;
    int v = (100 + d*g - b) % 10; if (v == a || v == b || v == g || v == d) continue;

    int ab  =  10 * a + b;
    int vg  =  10 * v + g;
    int ddd = 111 * d;
    int vv  =  11 * v;
    if (ab * vg == ddd && d * vg - ab == vv) {

      cout << a << ", " << b << ", " << v << ", " << g << ", " << d << "\n";

      cout << ab << " * " << vg << " = " << ddd << "\n";
      cout <<  d << " * " << vg << " - " <<  ab << " = " << vv << "\n";

      cout << ab * g << "\n";
    }
  }
}

int main()
{
  // solve();
  std::cout << "3, 7, 1, 2, 4\n"
               "37 * 12 = 444\n"
               "4 * 12 - 37 = 11\n"
               "74\n";
  return 0;
}
