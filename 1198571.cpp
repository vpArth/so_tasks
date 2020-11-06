#include <iostream>
using namespace std;


// a[n] = -1^n * x^(2n+1) / (2n)!
// (2n)! = (2n-2)!*(2n-1)*2n
// a[0] = x
// a[n] = a[n-1] * -1 * x*x / ((2n-1)*2n)
int main()
{
    int n;
    cout << "n=";
    n = 5;// cin >> n;
    double x;
    cout << "x=";
    x = 2;// cin >> x;

    double a = x, S = 0; //начальные значения

    cout << "\ni\t|\ta\t|\tS\n"; //заголовок таблицы
    for (int i = 1; i <= n; i++)
    {
        a *= -1 * (x*x) / (2*i*(2*i-1));
        S += a;
        cout << i << "\t| " << a << "\t| " << S << endl;
    }
    return 0;
}
