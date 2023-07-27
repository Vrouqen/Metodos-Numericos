from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from Proyecto.unidades.Unidad_1 import Unidad1

#Iniciar la aplicación
app=QtWidgets.QApplication([])

#Cargar archivos .ui
main=uic.loadUi("interfaz/VentanaMain.ui")
calcErrores=uic.loadUi("interfaz/CalculoErrores.ui")
sistNumeros=uic.loadUi("interfaz/SistemasNumeros.ui")
sistNumerosIEEE=uic.loadUi("interfaz/SistemasNumeracionIEEE.ui")
propagErrores=uic.loadUi("interfaz/PropagacionErrores.ui")
teoremaBolzano=uic.loadUi("interfaz/TeoremaBolzano.ui")
metodoBiseccion=uic.loadUi("interfaz/MetodoBiseccion.ui")

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
def regresarBiseccion():
    main.show()
    metodoBiseccion.hide()
def entrarBiseccion():
    metodoBiseccion.show()
    main.hide()

def cerrarPrograma():
    main.close()


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
        print("final")
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

def mostraGraficaPropagacionErrores():
    if validadorDecimales(propagErrores.textValorX.toPlainText()):
        valorXSup=float(propagErrores.textValorX.toPlainText())
        if valorXSup>0:
            Unidad1.graficaDeEcuacionPropagacionErrores(1, valorXSup)
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


def calcularTeoremaBolzano():
    if validadorDecimales(teoremaBolzano.textValorInf.toPlainText()) and validadorDecimales(teoremaBolzano.textValorSup.toPlainText()):
        valorInf=float(teoremaBolzano.textValorInf.toPlainText())
        valorSup=float(teoremaBolzano.textValorSup.toPlainText())
        if valorInf < valorSup:
            funcion=teoremaBolzano.textFuncion.toPlainText()
            respuesta=Unidad1.teoremaBolzano(valorInf,valorSup,funcion)
            if respuesta==True:
                teoremaBolzano.labelResultado.setText("Existe una raíz en el intervalo dado")
            else:
                teoremaBolzano.labelResultado.setText("No se encontró una raíz en el intervalo dado")
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Ingrese correctamente el intervalo")
            msg.exec_()
            teoremaBolzano.textValorInf.setText("")
            teoremaBolzano.textValorSup.setText("")
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("Ingrese correctamente los números")
        msg.exec_()
        teoremaBolzano.textValorInf.setText("")
        teoremaBolzano.textValorSup.setText("")

def mostrarGraficaFuncionBolzano():
    if validadorDecimales(teoremaBolzano.textValorInf.toPlainText()) and validadorDecimales(teoremaBolzano.textValorSup.toPlainText()):
        valorInf = float(teoremaBolzano.textValorInf.toPlainText())
        valorSup = float(teoremaBolzano.textValorSup.toPlainText())
        if valorInf < valorSup:
            funcion = teoremaBolzano.textFuncion.toPlainText()
            Unidad1.graficarFuncion(valorInf,valorSup,funcion)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Ingrese correctamente el intervalo")
            msg.exec_()
            teoremaBolzano.textValorInf.setText("")
            teoremaBolzano.textValorSup.setText("")
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("Ingrese correctamente los números")
        msg.exec_()
        teoremaBolzano.textValorInf.setText("")
        teoremaBolzano.textValorSup.setText("")

def mostrarGraficaFuncionBiseccion():
    validarInf=validadorDecimales(metodoBiseccion.textValorInf.toPlainText())
    validarSup=validadorDecimales(metodoBiseccion.textEdit.toPlainText())
    if validarInf==True and validarSup==True:
        valorInf = float(metodoBiseccion.textValorInf.toPlainText())
        valorSup = float(metodoBiseccion.textEdit.toPlainText())
        if valorInf < valorSup:
            funcion = metodoBiseccion.textFuncion.toPlainText()
            Unidad1.graficarFuncion(valorInf,valorSup,funcion)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Ingrese correctamente el intervalo")
            msg.exec_()
            metodoBiseccion.textValorInf.setText("")
            metodoBiseccion.textEdit.setText("")
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("Ingrese correctamente los números")
        msg.exec_()
        metodoBiseccion.textValorInf.setText("")
        metodoBiseccion.textEdit.setText("")

def calcularMétodoBisección():
    print(validadorDecimales(metodoBiseccion.textValorInf.toPlainText()))
    print(validadorDecimales(metodoBiseccion.textEdit.toPlainText()))
    if validadorDecimales(metodoBiseccion.textValorInf.toPlainText()) and validadorDecimales(metodoBiseccion.textEdit.toPlainText()):
        valorInf=float(metodoBiseccion.textValorInf.toPlainText())
        valorSup=float(metodoBiseccion.textEdit.toPlainText())
        if valorInf < valorSup:
            funcion=metodoBiseccion.textFuncion.toPlainText()
            respuesta=Unidad1.metodoBiseccion(valorInf,valorSup,0.0001,funcion)
            metodoBiseccion.labelResultado.setText("La raíz en el intervalo es "+str(respuesta))
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Ingrese correctamente el intervalo")
            msg.exec_()
            metodoBiseccion.textValorInf.setText("")
            metodoBiseccion.textValorSup.setText("")
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("Ingrese correctamente los números")
        msg.exec_()
        metodoBiseccion.textValorInf.setText("")
        metodoBiseccion.textEdit.setText("")

def ayuda():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setWindowTitle("Ayuda")
    msg.setText("Un ejemplo para insertar una ecuacion de buena forma es: (x**(3+2x))/x+3x**4")
    msg.exec_()
    metodoBiseccion.textValorInf.setText("")
    metodoBiseccion.textEdit.setText("")

#Asignación de funciones a botones de manejo de interfaz
main.botonCalError.clicked.connect(entrarCalcError) #Entrar a cálculo de errores
main.botonSistNum.clicked.connect(entrarSistNum) #Entrar a sistemas numericos
main.botonPuntoFlot.clicked.connect(entrarSistNumIEEE) #Entrar a punto flotante
main.botonPropError.clicked.connect(entrarPropagErrores) #Entrar a propagación de errores
main.botonBolzano.clicked.connect(entrarBolzano) #Entrar a Teorema de Bolzando
main.botonBiseccion.clicked.connect(entrarBiseccion)#entra a Metodo de Biseccion
main.botonSalir.clicked.connect(cerrarPrograma)#Sale del programa

calcErrores.botonRegresar.clicked.connect(regresarCalcError) #Regresar a main desde cálculo de errores
sistNumeros.botonRegresar.clicked.connect(regresarSistNum) #Regresar a main desde sistemas numericos
sistNumerosIEEE.botonRegresar.clicked.connect(regresarSistNumIEEE) #Regresar a main desde punto flotante
propagErrores.botonRegresar.clicked.connect(regresarPropagErrores) #Regresar a main desde propagación de errores
teoremaBolzano.botonRegresar.clicked.connect(regresarBolzano) #Regresar a main desde Teorema Bolzano
metodoBiseccion.botonRegresar.clicked.connect(regresarBiseccion)#Regresar a main desde Metodo Biseccion

#Asignación de funciones/utilidades
calcErrores.botonAbs.clicked.connect(calcularErrorAbs) #Calcular Error Absoluto
calcErrores.botonRelat.clicked.connect(calcularErrorRelativo) #Calcular Error Relativo

sistNumeros.botonBinToDec.clicked.connect(transformarBinarioToDecimal) #binario a decimal
sistNumeros.botonDecToBin.clicked.connect(transformarDecimalToBinario) #decimal a binario
sistNumeros.botonHexaToDec.clicked.connect(transfomarHexadecimalToDecimal) #hexadecimal a decimal
sistNumeros.botonOctToDec.clicked.connect(transformarOctalToDecimal) #octal a decimal

propagErrores.botonCalcular.clicked.connect(solucionDeEcuacion)#Solución de la ecuación (e^x)/(e^x -1)
propagErrores.botonGrafico.clicked.connect(mostraGraficaPropagacionErrores)#Grafica de la funcion

sistNumerosIEEE.boton32bits.clicked.connect(convertirIEE754_32bits)#Conversion de numero a IEE 754 32 bits
sistNumerosIEEE.boton64bits.clicked.connect(convertirIEE754_64bits)#Conversion de numero a IEE 754 64 bits

teoremaBolzano.botonCalcular.clicked.connect(calcularTeoremaBolzano)#Calcula el Teorema de bolzano
teoremaBolzano.botonGrafico.clicked.connect(mostrarGraficaFuncionBolzano)#Grafica del Teoreama de bolzano
teoremaBolzano.botonAyuda.clicked.connect(ayuda)#Boton de ayuda para ingresar la función

metodoBiseccion.botonCalcular.clicked.connect(calcularMétodoBisección)#Calcula el método de Bisección
metodoBiseccion.botonGrafico.clicked.connect(mostrarGraficaFuncionBiseccion)#Grafica del método de Bisección
metodoBiseccion.botonAyuda.clicked.connect(ayuda)#Boton de ayuda para ingresar la función

main.show()
app.exec()