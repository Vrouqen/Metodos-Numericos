import numpy as np
def count_values_in_range(N):
    count = np.nextafter(N+1, N) - N
    return count
N = 1  # Valor entero
values_count = count_values_in_range(N)
print("Número de valores representables en el intervalo [N, N+1]:", values_count)

