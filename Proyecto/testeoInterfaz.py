from PyQt5 import QtWidgets, uic

#Iniciar la aplicación
app=QtWidgets.QApplication([])

#Cargar archivos .ui
main=uic.loadUi("VentanaMain.ui")
calcErrores=uic.loadUi("CalculoErrores.ui")

def regresarMain():
    main.show()
    calcErrores.hide()

def entrarCalcError():
    calcErrores.show()
    main.hide()

#Funciones a botones
main.botonCalError.clicked.connect(entrarCalcError) #Entrar a cálculo de errores
calcErrores.botonRegresar.clicked.connect(regresarMain) #Regresar a main desde cálculo de errores

main.show()
app.exec()