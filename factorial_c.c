#include <stdio.h>
#include <time.h>

int factorial_recursivo(int n) {
    if (n == 0 || n == 1)
        return 1;
    return n * factorial_recursivo(n - 1);
}

int factorial_iterativo(int n) {
    int resultado = 1;
    for (int i = 2; i <= n; i++)
        resultado *= i;
    return resultado;
}

int main() {
    int n = 10;
    clock_t start, end;
    double tiempo;

    start = clock();
    factorial_recursivo(n);
    end = clock();
    tiempo = (double)(end - start) / CLOCKS_PER_SEC;
    printf("[Recursivo] Tiempo para %d!: %f segundos\n", n, tiempo);

    start = clock();
    factorial_iterativo(n);
    end = clock();
    tiempo = (double)(end - start) / CLOCKS_PER_SEC;
    printf("[Iterativo] Tiempo para %d!: %f segundos\n", n, tiempo);

    return 0;
}
