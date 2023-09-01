
class Unidad2:
    #TEMA 1 - Series de Taylor

    def transformarAFuncion(x, funcionStr):
        try:
            return eval(funcionStr)
        except:
            print("Ecuación mal ingresada")

    def seriesDeTaylor(funcionStr, punto, orden):
        resultado = 0
        for n in range(orden + 1):
            termino = Unidad2.transformarAFuncion(punto,funcionStr) * (punto - 0) ** n / Unidad2.factorial(n)
            resultado += termino
        return resultado

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * Unidad2.factorial(n - 1)