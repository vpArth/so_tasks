// gcc -masm=intel
#include <stdio.h>

int main()
{
    int dst;
    // an = 3* n^2 – 5 * n + 12, an > 1500
    // (3n-5)*n + 12
    asm (
        "xor ebx, ebx;"
        "xor ecx, ecx;"
        "it:"
        "lea eax, [ecx+ecx*2];"
        "sub eax, 5;"
        "mul ecx;"
        "add eax, 12;"

        "add ebx, eax;"

        "cmp ebx, 1500;"
        "jg res;"
        "inc ecx;"

        "jmp it;"
        "res:mov %0, ecx;"

        : "=r" (dst)
    );

    printf("%d\n", dst); // 12

    int sum = 0, n = 0;
    do {
        sum += (3*n-5)*n+12;
        if (sum > 1500) break;
        n++;
    } while (1);

    printf("%d %d\n", n, sum); // 12 1716
}
