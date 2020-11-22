#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define TAB_LEN (8)

char* solution(char *str) {
    int sn = strlen(str);

    // Считаем новый размер строки
    int n = 0;
    for (int i = 0, si = 0; i < sn; ++i) {
        int inc = 1;
        if (str[i] == '\t') {
            int rest = TAB_LEN - (si % TAB_LEN);
            inc = rest;
        }
        si += inc;
        n  += inc;
    }

    char* result = (char*) malloc(n+1);

    int ri = 0;
    // Заполняем новую строку
    for (int i = 0; i < sn; ++i) {
        if (str[i] == '\t') {
            int rest = TAB_LEN - (ri % TAB_LEN);
            while (rest--) result[ri++] = '*';
        } else {
            result[ri++] = str[i];
        }
    }

    result[ri++] = '\0';

    return result;
}

int main()
{
    char *src, *result;

    src = "\t12345\t123";
    result = solution(src);
    printf("%s\n%s\n", src, result);
    free(result);

    src = "1\t23\t123\t1234";
    result = solution(src);
    printf("%s\n%s\n", src, result);
    free(result);

    src = "|\t-- ID --\t-- TITLE --\t-- DATE -- \t|";
    result = solution(src);
    printf("%s\n%s\n", src, result);
    free(result);

    return 0;
}
