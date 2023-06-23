from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

from Unidad_1 import Unidad1

#Iniciar la aplicación
app=QtWidgets.QApplication([])

#Cargar archivos .ui
main=uic.loadUi("VentanaMain.ui")
calcErrores=uic.loadUi("CalculoErrores.ui")
sistNumeros=uic.loadUi("SistemasNumeros.ui")
sistNumerosIEEE=uic.loadUi("SistemasNumeracionIEEE.ui")
propagErrores=uic.loadUi("PropagacionErrores.ui")

#Funciones de manejo de interfaz
def regresarCalcError():
    main.show()
    calcErrores.hide()
def entrarCalcError():
    calcErrores.show()
    main.hide()

def regresarSistNum():
    main.show()
    sistNumeros.hide()
def entrarSistNum():
    sistNumeros.show()
    main.hide()

def regresarSistNumIEEE():
    main.show()
    sistNumerosIEEE.hide()
def entrarSistNumIEEE():
    sistNumerosIEEE.show()
    main.hide()

def regresarPropagErrores():
    main.show()
    propagErrores.hide()
def entrarPropagErrores():
    propagErrores.show()
    main.hide()

#Validaciones
def validadorDecimales(decimalString):
    try:
        decimal=float(decimalString)
    except:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("Ingrese correctamente el número")
        msg.exec_()
        #Hace falta terminar la ejecucion del metodo
    return decimal

def validarHexadecimales(numeroHexadecimal):
    try:
        int(numeroHexadecimal, 16)
    except ValueError:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("Ingrese correctamente el número hexadecimal")
        msg.exec_()
    return numeroHexadecimal

def validarOctales(numeroOctal):
    try:
        int(numeroOctal, 8)
    except ValueError:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("Ingrese correctamente el número octal")
        msg.exec_()
    return numeroOctal

#Funciones/utilidades
def calcularErrorAbs():
    valorReal=validadorDecimales(calcErrores.textReal.toPlainText())
    valorAproximado=validadorDecimales(calcErrores.textAprox.toPlainText())
    errorAbsoluto=Unidad1.calcularErrorAbsoluto(valorReal,valorAproximado)
    calcErrores.labelResultado.setText("Error absoluto: "+str(errorAbsoluto))

def calcularErrorRelativo():
    valorReal=validadorDecimales(calcErrores.textReal.toPlainText())
    valorAproximado=validadorDecimales(calcErrores.textAprox.toPlainText())
    errorRelativo=Unidad1.calcularErrorRelativo(valorReal,valorAproximado)
    calcErrores.labelResultado.setText("Error relativo: "+str(errorRelativo))

def transformarBinarioToDecimal():
    cadena=sistNumeros.textNumero.toPlainText()
    print(cadena)
    valido=False
    for i in cadena: #Validar correcto ingreso de binarios
        if i != '0' and i != '1':  # Mensaje de error
            valido=False
            break
        else:
            valido=True

    if valido==False: #Caso de no haber correctamente el binario
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("Unicamente es válido el ingreso de 0 y 1")
        msg.exec_()
    else:
        decimal=Unidad1.convertirBinarioToDecimal(cadena)
        sistNumeros.labelNumTransformado.setText(str(decimal))

def transformarDecimalToBinario():
    decimal=int(validadorDecimales(sistNumeros.textNumero.toPlainText()))
    binario=Unidad1.convertirDecimalToBinario(decimal) #Solo transforma números enteros
    sistNumeros.labelNumTransformado.setText(str(binario))

def transfomarHexadecimalToDecimal():
    hexadecimal=validarHexadecimales(sistNumeros.textNumero.toPlainText())
    decimal=Unidad1.convertirHexadecimalToDecimal(hexadecimal)
    sistNumeros.labelNumTransformado.setText(str(decimal))

def transformarOctalToDecimal():
    octal=int(validarOctales(sistNumeros.textNumero.toPlainText()))
    decimal=Unidad1.convertirOctalToDecimal(octal)
    sistNumeros.labelNumTransformado.setText(str(decimal))

def solucionDeEcuacion():
    valorX=float(validadorDecimales(propagErrores.textValorX.toPlainText()))
    if valorX>0:
        solucion=Unidad1.solucionDeEcuacion(valorX)
        propagErrores.labelResultado.setText(str(solucion))
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("Solo se aceptan numeros mayores a 0")
        msg.exec_()
        propagErrores.textValorX.setText("")

def mostraGrafica():
    valorX=float(validadorDecimales(propagErrores.textValorX.toPlainText()))
    if valorX>0:
        Unidad1.graficaDeEcuacion(valorX)
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("Solo se aceptan numeros mayores a 0")
        msg.exec_()
        propagErrores.textValorX.setText("")

def convertirIEE754_32bits():
    num=float(validadorDecimales(sistNumerosIEEE.textNumero.toPlainText()))
    convertido=Unidad1.convertirIEE754_32bits(num)
    sistNumerosIEEE.labelNumTransformado.setText(str(convertido))

def convertirIEE754_64bits():
    num=float(validadorDecimales(sistNumerosIEEE.textNumero.toPlainText()))
    convertido=Unidad1.convertirIEE754_64bits(num)
    sistNumerosIEEE.labelNumTransformado.setText(str(convertido))

#Asignación de funciones a botones de manejo de interfaz
main.botonCalError.clicked.connect(entrarCalcError) #Entrar a cálculo de errores
main.botonSistNum.clicked.connect(entrarSistNum) #Entrar a sistemas numericos
main.botonPuntoFlot.clicked.connect(entrarSistNumIEEE) #Entrar a punto flotante
main.botonPropError.clicked.connect(entrarPropagErrores) #Entrar a propagación de errores

calcErrores.botonRegresar.clicked.connect(regresarCalcError) #Regresar a main desde cálculo de errores
sistNumeros.botonRegresar.clicked.connect(regresarSistNum) #Regresar a main desde sistemas numericos
sistNumerosIEEE.botonRegresar.clicked.connect(regresarSistNumIEEE) #Entrar a punto flotante
propagErrores.botonRegresar.clicked.connect(regresarPropagErrores) #Entrar a propagación de errores


#Asignación de funciones/utilidades
calcErrores.botonAbs.clicked.connect(calcularErrorAbs) #Calcular Error Absoluto
calcErrores.botonRelat.clicked.connect(calcularErrorRelativo) #Calcular Error Relativo

sistNumeros.botonBinToDec.clicked.connect(transformarBinarioToDecimal) #binario a decimal
sistNumeros.botonDecToBin.clicked.connect(transformarDecimalToBinario) #decimal a binario
sistNumeros.botonHexaToDec.clicked.connect(transfomarHexadecimalToDecimal) #hexadecimal a decimal
sistNumeros.botonOctToDec.clicked.connect(transformarOctalToDecimal) #octal a decimal

propagErrores.botonCalcular.clicked.connect(solucionDeEcuacion)#Solución de la ecuación (e^x)/(e^x -1)
propagErrores.botonGrafico.clicked.connect(mostraGrafica)#Grafica de la funcion

sistNumerosIEEE.boton32bits.clicked.connect(convertirIEE754_32bits)#Conversion de numero a IEE 754 32 bits
sistNumerosIEEE.boton64bits.clicked.connect(convertirIEE754_64bits)#Conversion de numero a IEE 754 64 bits

main.show()
app.exec()