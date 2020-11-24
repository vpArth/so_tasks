// gcc -masm=intel
#include <stdio.h>

int main()
{
    int dst;
    // an = 3* n^2 – 5 * n + 12, an > 1500
    // (3n-5)*n + 12
    asm (
        "mas dw 0,1,2,3,4;"
        "mov si,3;"
        "mov ax,mas[si];"
        "mov %0, ax"

        : "=r" (dst)
    );

    printf("%d\n", dst); // 12
}
