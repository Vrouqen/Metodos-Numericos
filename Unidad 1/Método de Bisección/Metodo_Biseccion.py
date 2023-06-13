import matplotlib.pyplot as plt
import sys
def metodoBiseccion(funcion, a, b, precision):
    if funcion(a) * funcion(b) >= 0:
        print("La función en el punto A debe ser de signo opuesto a el punto B")
        sys.exit()
    while (b - a) / 2 > precision:
        c = (a + b) / 2
        if funcion(c) == 0:
            return c
        elif funcion(a) * funcion(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def f(x):
    return x**2 - 8

print("Función a evaluar f(x) = x^2 - 8")
# Intervalo para verificar la existencia de una raíz
a=float(input("Ingrese el valor inicial del intervalo > "))
b=float(input("Ingrese el valor final del intervalo > "))
if b<a:
    print("Intervalo mal ingresado")
    sys.exit()
r = metodoBiseccion(f, a, b, 0.0001)
print("La raíz aproximada es:", r)
#Grafica de función
print()
mostrarGrafico=input("Ingrese 's' para mostrar el gráfico > ")
if mostrarGrafico == "s":
    valorX = a
    valoresY = []
    valoresX = []
    while valorX <= b:
        valoresX.append([valorX])  # arreglo de valores de x
        valoresY.append([f(valorX)])  # arreglo de valores en y con respectivo cálculo
        valorX += 0.1  # Incremento pequeño para mostrar más presición en el gráfico
    plt.plot(valoresX, valoresY)  # Se crea el gráfico
    plt.plot([0,b],[0,0], color='black') #Dibuja la linea del eje X
    plt.plot([0,0],[f(a),f(b)], color='black') #Dibuja la linea del eje Y
    plt.show()  # Se imprime el gráfico