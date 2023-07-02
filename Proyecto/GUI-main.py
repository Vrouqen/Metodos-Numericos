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
teoremaBolzano=uic.loadUi("TeoremaBolzano.ui")

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

def regresarBolzano():
    main.show()
    teoremaBolzano.hide()
def entrarBolzano():
    teoremaBolzano.show()
    main.hide()


#Validaciones
def validadorEnteros(decimalString):
    try:
        decimal=int(decimalString)
        validado=True
    except:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("Ingrese correctamente el número")
        msg.exec_()
        validado=False
        #Hace falta terminar la ejecucion del metodo
    return validado

def validadorDecimales(decimalString):
    try:
        decimal=float(decimalString)
        validado=True
    except:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("Ingrese correctamente el número")
        msg.exec_()
        validado=False
        #Hace falta terminar la ejecucion del metodo
    return validado

def validarHexadecimales(numeroHexadecimal):
    try:
        int(numeroHexadecimal, 16)
        validado=True
    except ValueError:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("Ingrese correctamente el número hexadecimal")
        msg.exec_()
        validado=False
    return validado

def validarOctales(numeroOctal):
    try:
        int(numeroOctal, 8)
        validado=True
    except ValueError:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("Ingrese correctamente el número octal")
        msg.exec_()
        validado=False
    return validado

#Funciones/utilidades
def calcularErrorAbs():
    correcto1=validadorDecimales(calcErrores.textReal.toPlainText())
    correcto2=validadorDecimales(calcErrores.textAprox.toPlainText())
    if correcto1==True and correcto2==True:
        valorReal=float(calcErrores.textReal.toPlainText())
        valorAproximado=float(calcErrores.textAprox.toPlainText())
        errorAbsoluto=Unidad1.calcularErrorAbsoluto(valorReal,valorAproximado)
        calcErrores.labelResultado.setText("Error absoluto: "+str(errorAbsoluto))
    else:
        calcErrores.textReal.setText("")
        calcErrores.textAprox.setText("")

def calcularErrorRelativo():
    correcto1=validadorDecimales(calcErrores.textReal.toPlainText())
    correcto2=validadorDecimales(calcErrores.textAprox.toPlainText())
    if correcto1==True and correcto2==True:
        valorReal=float(calcErrores.textReal.toPlainText())
        valorAproximado=float(calcErrores.textAprox.toPlainText())
        errorRelativo=Unidad1.calcularErrorRelativo(valorReal,valorAproximado)
        calcErrores.labelResultado.setText("Error relativo: "+str(errorRelativo))
    else:
        calcErrores.textReal.setText("")
        calcErrores.textAprox.setText("")

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
        sistNumeros.textNumero.setText("")
    else:
        decimal=Unidad1.convertirBinarioToDecimal(cadena)
        sistNumeros.labelNumTransformado.setText(str(decimal))

def transformarDecimalToBinario():
    if validadorEnteros(sistNumeros.textNumero.toPlainText()):
        decimal=int(sistNumeros.textNumero.toPlainText())
        binario=Unidad1.convertirDecimalToBinario(decimal) #Solo transforma números enteros
        sistNumeros.labelNumTransformado.setText(str(binario))
    else:
        sistNumeros.textNumero.setText("")

def transfomarHexadecimalToDecimal():
    if validadorEnteros(sistNumeros.textNumero.toPlainText()):
        hexadecimal=int(sistNumeros.textNumero.toPlainText())
        decimal=Unidad1.convertirHexadecimalToDecimal(hexadecimal)
        sistNumeros.labelNumTransformado.setText(str(decimal))
    else:
        sistNumeros.textNumero.setText("")

def transformarOctalToDecimal():
    if validadorEnteros(sistNumeros.textNumero.toPlainText()):
        octal = int(sistNumeros.textNumero.toPlainText())
        decimal=Unidad1.convertirOctalToDecimal(octal)
        sistNumeros.labelNumTransformado.setText(str(decimal))
    else:
        sistNumeros.textNumero.setText("")

def solucionDeEcuacion():
    if validadorDecimales(propagErrores.textValorX.toPlainText()):
        valorX = float(propagErrores.textValorX.toPlainText())
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
    else:
        propagErrores.textValorX.setText("")

def mostraGrafica():
    if validadorDecimales(propagErrores.textValorX.toPlainText()):
        valorX=float(propagErrores.textValorX.toPlainText())
        if valorX>0:
            Unidad1.graficaDeEcuacion(valorX)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Solo se aceptan numeros mayores a 0")
            msg.exec_()
            propagErrores.textValorX.setText("")
    else:
        propagErrores.textValorX.setText("")

def convertirIEE754_32bits():
    if validadorDecimales(sistNumerosIEEE.textNumero.toPlainText()):
        num=float(sistNumerosIEEE.textNumero.toPlainText())
        convertido=Unidad1.convertirIEE754_32bits(num)
        sistNumerosIEEE.labelNumTransformado.setText(str(convertido))
    else:
        sistNumerosIEEE.textNumero.setText("")
def convertirIEE754_64bits():
    if validadorDecimales(sistNumerosIEEE.textNumero.toPlainText()):
        num=float(sistNumerosIEEE.textNumero.toPlainText())
        convertido=Unidad1.convertirIEE754_64bits(num)
        sistNumerosIEEE.labelNumTransformado.setText(str(convertido))
    else:
        sistNumerosIEEE.textNumero.setText("")

#Asignación de funciones a botones de manejo de interfaz
main.botonCalError.clicked.connect(entrarCalcError) #Entrar a cálculo de errores
main.botonSistNum.clicked.connect(entrarSistNum) #Entrar a sistemas numericos
main.botonPuntoFlot.clicked.connect(entrarSistNumIEEE) #Entrar a punto flotante
main.botonPropError.clicked.connect(entrarPropagErrores) #Entrar a propagación de errores
main.botonBolzano.clicked.connect(entrarBolzano) #Entrar a Teorema de Bolzando

calcErrores.botonRegresar.clicked.connect(regresarCalcError) #Regresar a main desde cálculo de errores
sistNumeros.botonRegresar.clicked.connect(regresarSistNum) #Regresar a main desde sistemas numericos
sistNumerosIEEE.botonRegresar.clicked.connect(regresarSistNumIEEE) #Regresar a main desde punto flotante
propagErrores.botonRegresar.clicked.connect(regresarPropagErrores) #Regresar a main desde propagación de errores
teoremaBolzano.botonRegresar.clicked.connect(regresarBolzano) #Regresar a main desde Teorema Bolzano

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