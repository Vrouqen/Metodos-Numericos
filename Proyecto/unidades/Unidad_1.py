#!pip install PyQT5

import struct #Conversiones de formato IEE 754
import math #Propagación de errores
import matplotlib.pyplot as plt #Gráficos
from Proyecto.unidades.Archivos import ManejoArchivos

class Unidad1:

    #TEMA 1 - CALCULO DE ERRORES
    #Calculo de error absoluto
    def calcularErrorAbsoluto(valorReal, valorAproximado):
        errorAbsoluto=abs(valorReal-valorAproximado)
        ManejoArchivos.almacenarDatosErrores(1,valorReal,valorAproximado,errorAbsoluto)
        return errorAbsoluto

    #Calculo de error relativo
    def calcularErrorRelativo(valorReal, valorAproximado):
      errorRelativo=abs(valorReal-valorAproximado)/abs(valorReal)
      ManejoArchivos.almacenarDatosErrores(2,valorReal,valorAproximado,errorRelativo)
      return errorRelativo

    #TEMA 2 - SISTEMAS DE NUMERACION
    #Transformar número de binario a decimal
    def convertirBinarioToDecimal(numBinario):
        numBinarioAlmacenar=numBinario
        numero_decimal=0
        cantDigitos=len(numBinario)
        for i in range(cantDigitos):
            digito=int(numBinario[cantDigitos - i - 1])
            numero_decimal+=digito*(2 ** i)
        ManejoArchivos.almacenarDatosSistemasNumeracion(1,numBinarioAlmacenar,numero_decimal)
        return numero_decimal

    #Transformar número de decimal a binario
    def convertirDecimalToBinario(numDecimal):
        numDecimalAlmacenar=numDecimal
        numBinario=""
        if numDecimal==0:
            numBinario="0"
        while numDecimal>0:
            bit=numDecimal%2
            numBinario=str(bit)+numBinario
            numDecimal//= 2
        ManejoArchivos.almacenarDatosSistemasNumeracion(2, numDecimalAlmacenar, numBinario)
        return numBinario

    #Transformar número hexadecimal a decimal
    def convertirHexadecimalToDecimal(numHexadecimal):
        numHexadecimalAlmacenar=numHexadecimal
        digitos="0123456789ABCDEF"
        numDecimal=0
        potencia=len(numHexadecimal)-1
        for digito in numHexadecimal:
            valor=digitos.index(digito)
            numDecimal+=valor*(16 ** potencia)
            potencia-=1
        ManejoArchivos.almacenarDatosSistemasNumeracion(3, numHexadecimalAlmacenar, numDecimal)
        return numDecimal

    #Transformar de número octal a decimal
    def convertirOctalToDecimal(numOctal):
        numOctalAlmacenar=numOctal
        numDecimal=0
        potencia=0
        while numOctal!=0:
            digito=numOctal % 10
            numDecimal+=digito*(8 ** potencia)
            numOctal//=10
            potencia+=1
        ManejoArchivos.almacenarDatosSistemasNumeracion(4, numOctalAlmacenar, numDecimal)
        return numDecimal

    #TEMA 3 - PUNTO FLOTANTE
    #Conversion de numero a IEE 754 32 bits
    def convertirIEE754_32bits(num):
      num1 = struct.pack('!f', num)
      numBinario = ''.join(format(byte, '08b') for byte in num1)
      ManejoArchivos.almacenarDatosIEE(1, num, numBinario)
      return numBinario

    #Conversion de numero a IEE 754 64 bits
    def convertirIEE754_64bits(num):
      num1 = struct.pack('!d', num)
      numBinario = ''.join(format(byte, '08b') for byte in num1)
      ManejoArchivos.almacenarDatosIEE(2, num, numBinario)
      return numBinario

    #TEMA 4 - PROPAGACION DE ERRORES
    #Solución de la ecuación (e^x)/(e^x -1)
    def solucionDeEcuacion(x):
        try:
            numerador = math.exp(x)
            denominador = math.exp(x) - 1
            resultado = numerador / denominador
            ManejoArchivos.almacenarDatosPropagacion(x,resultado)
            return resultado
        except Exception as e:
            print("Error en el cálculo: ", str(e))

    #Gráfica de la ecuación (e^x)/(e^x -1)
    def graficaDeEcuacionPropagacionErrores(valorIncialX, valorFinalX):
        if(valorFinalX>valorIncialX):
            valorX=valorIncialX
            valoresY=[]
            valoresX=[]
            while valorX<=valorFinalX:
                valoresX.append([valorX]) #arreglo de valores de x
                valoresY.append([Unidad1.solucionDeEcuacion(valorX)]) #arreglo de valores en y con respectivo cálculo
                valorX+=0.1 #Incremento pequeño para mostrar más presición en el gráfico
            plt.plot(valoresX,valoresY) #Se crea el gráfico
            plt.show() #Se imprime el gráfico
        else:
            print("No es válido un número menor a 1")

    #TEMA 5 - TEOREMA DE BOLZANO
    def transformarAFuncion(x, funcionStr):
        try:
            return eval(funcionStr)
        except:
            print("Ecuación mal ingresada")

    def graficarFuncion(valorIncialX, valorFinalX, funcion):
        valorX=valorIncialX
        valoresX=[]
        valoresY=[]
        while valorX<=valorFinalX:
            valoresX.append([valorX])  # arreglo de valores de x
            valoresY.append([Unidad1.transformarAFuncion(valorX,funcion)])  # arreglo de valores en y con respectivo cálculo
            valorX += 0.1  # Incremento pequeño para mostrar más presición en el gráfico
        plt.plot(valoresX, valoresY)  # Se crea el gráfico
        valorYInf = Unidad1.transformarAFuncion(valorIncialX, funcion)
        valorYSup = Unidad1.transformarAFuncion(valorFinalX, funcion)
        if valorIncialX <= 0 and valorFinalX >= 0:
            plt.plot([valorIncialX, valorFinalX], [0, 0], color='black')  # Dibuja la linea del eje X
        if valorYInf <= 0 and valorYSup >= 0:
            plt.plot([0, 0], [valorYInf, valorYSup], color='black')  # Dibuja la linea del eje Y
        plt.show()  # Se imprime el gráfico

    def teoremaBolzano(valorInf, valorSup, funcion):
        valorYInf=Unidad1.transformarAFuncion(valorInf,funcion)
        valorYSup=Unidad1.transformarAFuncion(valorSup,funcion)
        if valorYInf * valorYSup < 0:
            raiz=True
        else:
            raiz=False
        ManejoArchivos.almacenarDatosBolzano(valorInf,valorSup,funcion,raiz)
        return raiz

    #TEMA 6 - METODO DE BISECCION
    def metodoBiseccion(valorInf, valorSup, precision, funcion):
        valorYInf=Unidad1.transformarAFuncion(valorInf,funcion)
        valorYSup=Unidad1.transformarAFuncion(valorSup,funcion)
        while (valorSup-valorInf)/2 > precision:
            c = (valorInf+valorSup)/2
            valorYC=Unidad1.transformarAFuncion(c,funcion)
            if valorYC == 0:
                return c
            elif valorYInf*valorYC<0:
                valorSup=c
            else:
                valorInf=c
        resultado=(valorInf + valorSup) / 2
        return resultado