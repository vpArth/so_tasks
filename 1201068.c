#include <stdio.h>
#include <math.h>

void solution(int n) {
    if (n == 0) return;
    solution(n - 1);
    int i = ceil((1+sqrt(1+8*n))/2) - 1; // Ищем индекс треугольного числа
    printf("%d ", i);
}
int main(int argc, char *argv[])
{
    solution(57);
    printf("\n");
}

/*

Tn = 0.5 * n * (n-1)
2Tn = n**2 - n
n**2 - n - 2Tn = 0
D = 1 + 8Tn
x = 1/2 * 1 + sqrt(1+8Tn)

1 1
2 2
3 2
4 3
5 3
6 3
7 4
8 4
9 4
a 4
*/
