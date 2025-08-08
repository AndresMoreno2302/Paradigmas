import time
import matplotlib.pyplot as plt

def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursivo(n - 1)

def factorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

n_values = list(range(1, 100))
tiempos_r = []
tiempos_i = []

for n in n_values:
    start = time.time()
    factorial_recursivo(n)
    tiempos_r.append(time.time() - start)

    start = time.time()
    factorial_iterativo(n)
    tiempos_i.append(time.time() - start)

plt.plot(n_values, tiempos_r, label="Recursivo")
plt.plot(n_values, tiempos_i, label="Iterativo")
plt.xlabel("n")
plt.ylabel("Tiempo de ejecución (s)")
plt.title("Comparación de Tiempo: Recursivo vs Iterativo")
plt.legend()
plt.grid(True)
plt.savefig("comparacion_tiempos.png")
plt.show()
