
class Examen:

    #Tema 1 - Espacios duales


    #Tema 2 - Base dual

    #Tema 3 - Interpolación polinómica lagrange
    def interpolacionPolinomicaLagrange(valoresX, valoresY):
        def interpolate(x):
            n = len(valoresX)
            valorInterpolado = 0.0
            for i in range(n):
                termino = valoresY[i]
                for j in range(n):
                    if i != j:
                        termino *= (x - valoresX[j]) / (valoresX[i] - valoresX[j])
                valorInterpolado += termino
            return valorInterpolado
        return interpolate


