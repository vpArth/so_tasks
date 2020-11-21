#include <stdio.h>

void input(int *arr, size_t N, size_t M) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            printf("Vvedit znachennya A%d,%d = ", i+1, j+1);
            scanf("%d", &arr[i*M+j]);
        };
        printf("\n");
    };
}

void doSomething(int *arr, size_t N, size_t M) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            arr[i*M + j] = (i+j) * arr[i*M + j];
        };
    };
}

void print(int *arr, size_t N, size_t M) {
    for (int i = 0; i < N; i++) {
        printf("[");
        for (int j = 0; j < M; j++) {
            printf("\'%d\'", arr[i*M+j]);
            if (j < M - 1) {
                printf(", ");
            }
        };
        printf("]\n");
    };
}

int main() {
    size_t M, N;
    scanf("%lu %lu", &M, &N);
    int array[N][M];

    input((int*)(array), N, M);
    print((int*)array, N, M);

    printf("Do something\n");
    doSomething((int*)array, N, M);
    print((int*)array, N, M);
};

// gcc -Wall 1204765.c -o 1204765 && ./1204765 <<< '3 3 1 2 3 1 2 3 1 2 3'
