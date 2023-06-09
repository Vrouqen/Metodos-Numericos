import math
import matplotlib.pyplot as plt
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

#Gráfica de la función
print()
valorFinalX = float(input("Ingrese el valor final de X para ver su gráfico: "))
if(valorFinalX>1):
    valorX=1
    valoresY=[]
    valoresX=[]
    while valorX<=valorFinalX:
        valoresX.append([valorX]) #arreglo de valores de x
        valoresY.append([calcular_expresion(valorX)]) #arreglo de valores en y con respectivo cálculo
        valorX+=0.1 #Incremento pequeño para mostrar más presición en el gráfico
    plt.plot(valoresX,valoresY) #Se crea el gráfico
    plt.show() #Se imprime el gráfico
else:
    print("No es válido un número menor a 1")