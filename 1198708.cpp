#include <iostream>
#include <cmath>
#include <tuple>

double solve(double a, double p, double precision) {
    double prev, cur = 1;
    do {
        std::tie(prev, cur) = std::make_tuple(cur, ((p-1) * cur + a / std::pow(cur, p-1)) / p);
    } while (std::abs(cur - prev) > precision);

    return cur;
}

int main() {
    double precision, a, p;
    // std::cout << "Enter a value of precision : " << std::endl;
    // std::cin >> precision;
    // std::cout << "Enter a value of a : " << std::endl;
    // std::cin >> a;
    // std::cout << "Enter a value of p : " << std::endl;
    // std::cin >> p;

    precision = 1e-4;
    a = 5*5*5*5;
    p = 4;


    double solution = solve(a, p, precision);

    std::cout << a << " ^ 1/" << p << " = " << solution << "\n";

    return 0;
}
