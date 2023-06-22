from PyQt5 import QtWidgets, uic
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

#Funciones/utilidades
def calcularErrorAbs():
    valorReal=float(calcErrores.textReal.toPlainText())
    valorAproximado=float(calcErrores.textAprox.toPlainText())
    errorAbsoluto=Unidad1.calcularErrorAbsoluto(valorReal,valorAproximado)
    calcErrores.labelResultado.setText("Error absoluto: "+str(errorAbsoluto))

def calcularErrorRelativo():
    valorReal=float(calcErrores.textReal.toPlainText())
    valorAproximado=float(calcErrores.textAprox.toPlainText())
    errorRelativo=Unidad1.calcularErrorRelativo(valorReal,valorAproximado)
    calcErrores.labelResultado.setText("Error relativo: "+str(errorRelativo))


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

main.show()
app.exec()