#!pip install PyQT5

import struct #Conversiones de formato IEE 754
import math #Propagación de errores
import matplotlib.pyplot as plt #Gráficos

class Unidad1:

    #TEMA 1 - CALCULO DE ERRORES
    #Calculo de error absoluto
    def calcularErrorAbsoluto(valorReal, valorAproximado):
      errorAbsoluto=abs(valorReal-valorAproximado)
      return errorAbsoluto

    #Calculo de error relativo
    def calcularErrorRelativo(valorReal, valorAproximado):
      errorRelativo=Unidad1.calcularErrorAbsoluto(valorReal,valorAproximado)/abs(valorReal)
      return errorRelativo

    #TEMA 2 - SISTEMAS DE NUMERACION
    #Transformar número de binario a decimal
    def convertirBinarioToDecimal(numBinario):
        numero_decimal=0
        cantDigitos=len(numBinario)
        for i in range(cantDigitos):
            digito=int(numBinario[cantDigitos - i - 1])
            numero_decimal+=digito*(2 ** i)
        return numero_decimal

    #Transformar número de decimal a binario
    def convertirDecimalToBinario(numDecimal):
        numBinario=""
        if numDecimal==0:
            numBinario="0"
        while numDecimal>0:
            bit=numDecimal%2
            numBinario=str(bit)+numBinario
            numDecimal//= 2
        return numBinario

    #Transformar número hexadecimal a decimal
    def convertirHexadecimalToDecimal(numHexadecimal):
        digitos="0123456789ABCDEF"
        numDecimal=0
        potencia=len(numHexadecimal)-1
        for digito in numHexadecimal:
            valor=digitos.index(digito)
            numDecimal+=valor*(16 ** potencia)
            potencia-=1
        return numDecimal

    #Transformar de número octal a decimal
    def convertirOctalToDecimal(numOctal):
        numDecimal=0
        potencia=0
        while numOctal!=0:
            digito=numOctal % 10
            numDecimal+=digito*(8 ** potencia)
            numOctal//=10
            potencia+=1
        return numDecimal

    #TEMA 3 - PUNTO FLOTANTE
    #Conversion de numero a IEE 754 32 bits
    def convertirIEE754_32bits(num):
      num1 = struct.pack('!f', num)
      numBinario = ''.join(format(byte, '08b') for byte in num1)
      return numBinario

    #Conversion de numero a IEE 754 64 bits
    def convertirIEE754_64bits(num):
      num1 = struct.pack('!d', num)
      numBinario = ''.join(format(byte, '08b') for byte in num1)
      return numBinario

    #TEMA 4 - PROPAGACION DE ERRORES
    #Solución de la ecuación (e^x)/(e^x -1)
    def solucionDeEcuacion(x):
        numerador = math.exp(x)
        denominador = math.exp(x) - 1
        resultado = numerador / denominador
        return resultado

        valorX = float(validadorDecimales(propagErrores.textValorX.toPlainText()))
        if valorX > 0:
            if len(str(valorX)) <= 6:  # Verificar si el valor tiene hasta 6 dígitos
                solucion = Unidad1.solucionDeEcuacion(valorX)
                propagErrores.labelResultado.setText(str(solucion))
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Error")
                msg.setText("Solo se aceptan números de hasta 6 dígitos")
                msg.exec_()
                propagErrores.textValorX.setText("")
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Solo se aceptan números mayores a 0")
            msg.exec_()
            propagErrores.textValorX.setText("")

    #Gráfica de la ecuación (e^x)/(e^x -1)
    def graficaDeEcuacion(valorFinalX):
        if(valorFinalX>1):
            valorX=1
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

    #TEMA 6 - METODO DE BISECCION