
class Unidad2:
    #TEMA 1 - Series de Taylor
    def factorial(n):
        # Calcula el factorial de un número entero n
        if n == 0:
            return 1
        else:
            return n * Unidad2.factorial(n - 1)
    def transformarAFuncion(x, funcionStr):
        try:
            return eval(funcionStr)
        except:
            print("Ecuación mal ingresada")

    def derivadaEnesima(funcionStr, n, x):
        # Calcula la n-ésima derivada de la función en el punto x
        h = 1e-5  # Un valor pequeño para el cálculo numérico de la derivada
        return (Unidad2.transformarAFuncion(x + h*n,funcionStr) - Unidad2.transformarAFuncion(x,funcionStr))/ (h ** n)

    def calcularSeriesTaylor(funcionStr, punto, x, n):
        # Calcula la aproximación de la función en el punto utilizando n términos de la serie de Taylor
        aproximacion = 0
        for i in range(n + 1):
            aproximacion += Unidad2.derivadaEnesima(funcionStr, i, punto) * (x - punto) ** i / Unidad2.factorial(i)
        return aproximacion
