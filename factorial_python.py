import time
from memory_profiler import memory_usage

def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursivo(n - 1)

def factorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def medir_tiempos(n):
    start = time.time()
    factorial_recursivo(n)
    tiempo_r = time.time() - start

    start = time.time()
    factorial_iterativo(n)
    tiempo_i = time.time() - start

    print(f"[Recursivo] Tiempo para {n}!: {tiempo_r:.8f} s")
    print(f"[Iterativo] Tiempo para {n}!: {tiempo_i:.8f} s")

def medir_memoria(n):
    memoria_r = memory_usage((factorial_recursivo, (n,)), max_iterations=1)
    memoria_i = memory_usage((factorial_iterativo, (n,)), max_iterations=1)

    print(f"[Recursivo] Memoria para {n}!: {max(memoria_r) - min(memoria_r):.8f} MiB")
    print(f"[Iterativo] Memoria para {n}!: {max(memoria_i) - min(memoria_i):.8f} MiB")

if __name__ == "__main__":
    n = 10
    medir_tiempos(n)
    medir_memoria(n)
