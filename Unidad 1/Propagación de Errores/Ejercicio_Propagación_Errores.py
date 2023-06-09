import math
def calcular_expresion(x):
    numerador = math.exp(x)
    denominador = math.exp(x) - 1
    resultado = numerador / denominador
    return resultado

def solicitar_valor():
    while True:
        try:
            x = float(input("Ingresa un valor mayor a 250: "))
            if x > 250:
                return x
            else:
                print("El valor debe ser mayor a 250. Inténtalo nuevamente.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Solicitar el valor mayor a 250
valor = solicitar_valor()

# Calcular y mostrar el resultado
resultado = calcular_expresion(valor)
print("El resultado de la expresión para x = {} es: {}".format(valor, resultado))