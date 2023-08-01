import sys
from PySide2.QtCore import QPropertyAnimation
from PySide2 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from Proyecto.unidades.Unidad_1 import Unidad1
import matplotlib.pyplot as plt #Gráficos
#Iniciar la aplicación
app=QtWidgets.QApplication([])
main=uic.loadUi("ventana_principal.ui")
calcErrores=uic.loadUi("interfaz\CalculoErrores.ui")
def cerrar():
    main.close()


main.bt_uno.clicked.connect(lambda : main.stackedWidget.setCurrentWidget(main.page))
main.bt_dos.clicked.connect(lambda : main.stackedWidget.setCurrentWidget(main.page_uno))
main.bt_tres.clicked.connect(lambda : main.stackedWidget.setCurrentWidget(main.page_dos))
main.bt_cuatro.clicked.connect(lambda : main.stackedWidget.setCurrentWidget(main.page_tres))
main.bt_cinco.clicked.connect(lambda : main.stackedWidget.setCurrentWidget(main.page_cuatro))
main.bt_seis.clicked.connect(lambda : main.stackedWidget.setCurrentWidget(main.page_cinco))

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

def calcularErrorAbs():
    correcto1=validadorDecimales(main.textReal.toPlainText())
    correcto2=validadorDecimales(main.textAprox.toPlainText())
    if correcto1==True and correcto2==True:
        valorReal=float(main.textReal.toPlainText())
        valorAproximado=float(main.textAprox.toPlainText())
        errorAbsoluto=Unidad1.calcularErrorAbsoluto(valorReal,valorAproximado)
        main.labelResultado.setText("Error absoluto: "+str(errorAbsoluto))
        print("final")
    else:
        main.textReal.setText("")
        main.textAprox.setText("")

def calcularErrorRelativo():
    correcto1=validadorDecimales(main.textReal.toPlainText())
    correcto2=validadorDecimales(main.textAprox.toPlainText())
    if correcto1==True and correcto2==True:
        valorReal=float(main.textReal.toPlainText())
        valorAproximado=float(main.textAprox.toPlainText())
        errorRelativo=Unidad1.calcularErrorRelativo(valorReal,valorAproximado)
        main.labelResultado.setText("Error relativo: "+str(errorRelativo))
    else:
        main.textReal.setText("")
        main.textAprox.setText("")

#Propagacion de errores
def solucionDeEcuacion():
    if validadorDecimales(main.textValorX.toPlainText()):
        valorX = float(main.textValorX.toPlainText())
        if valorX > 0:
            if len(str(valorX)) <= 6:  # Verificar si el valor tiene hasta 6 dígitos
                solucion = Unidad1.solucionDeEcuacion(valorX)
                main.labelResultado_2.setText(str(solucion))
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Error")
                msg.setText("Solo se aceptan números de hasta 6 dígitos")
                msg.exec_()
                main.textValorX.setText("")
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Solo se aceptan números mayores a 0")
            msg.exec_()
            main.textValorX.setText("")
    else:
        main.textValorX.setText("")

def mostraGraficaPropagacionErrores():
    if validadorDecimales(main.textValorX.toPlainText()):
        valorXSup=float(main.textValorX.toPlainText())
        if valorXSup>0:
            Unidad1.graficaDeEcuacionPropagacionErrores(1, valorXSup)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Solo se aceptan numeros mayores a 0")
            msg.exec_()
            main.textValorX.setText("")
    else:
        main.textValorX.setText("")

#Asignación de funciones/utilidades
main.botonAbs.clicked.connect(calcularErrorAbs) #Calcular Error Absoluto
main.botonRelat.clicked.connect(calcularErrorRelativo) #Calcular Error Relativo

main.botonCalcular.clicked.connect(solucionDeEcuacion)#Solución de la ecuación (e^x)/(e^x -1)
main.botonGrafico.clicked.connect(mostraGraficaPropagacionErrores)#Grafica de la funcion

main.show()
app.exec()