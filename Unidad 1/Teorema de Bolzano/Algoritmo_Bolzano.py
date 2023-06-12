import matplotlib.pyplot as plt
def teoremaBolzano(f, a, b):
    fa = f(a)
    fb = f(b)
    # Se comprueba si los extremos del intervalo tienen signos opuestos
    if fa * fb < 0:
        return True
    else:
        return False

#Ejemplo de función
def f(x):
    return x**3 - x**2 + 2

print("Función a evaluar f(x) = x^3 - x^2 + 2")
# Intervalo para verificar la existencia de una raíz
a=float(input("Ingrese el valor inicial del intervalo > "))
b=float(input("Ingrese el valor final del intervalo > "))
if b>a:
    raiz_existe = teoremaBolzano(f, a, b)
    #Impresión de resultado
    if raiz_existe:
        print("Existe una raíz en el intervalo dado.")
    else:
        print("No se encontró una raíz en el intervalo dado.")
else:
    print("Intervalo mal ingresado")

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
    plt.plot([a,b],[0,0], color='black') #Dibuja la linea del eje X
    plt.plot([0,0],[f(a),f(b)], color='black') #Dibuja la linea del eje Y
    plt.show()  # Se imprime el gráfico
