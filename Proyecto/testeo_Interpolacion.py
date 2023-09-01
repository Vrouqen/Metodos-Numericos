import sys
from PySide2.QtCore import QPropertyAnimation
from PySide2 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from Proyecto.unidades.Unidad_1 import Unidad1
import matplotlib.pyplot as plt #Gráficos

from unidades.Examen import Examen

#Iniciar la aplicación
app=QtWidgets.QApplication([])
interpolacion=uic.loadUi("interfaz\InterpolacionLagrange.ui")

def resolverinter():
    if len(Examen.valoresX)!=0 and len(Examen.valoresY)!=0:
        try:
            valorX=float(interpolacion.textValorX2.toPlainText())
            valoresX=Examen.valoresX
            valoresY=Examen.valoresY
            funcionInterpolada = Examen.interpolacionPolinomicaLagrange(valoresX, valoresY)
            valorInterpolado = valorX
            resultado = funcionInterpolada(valorInterpolado)
            interpolacion.labelResultado.setText("El valor interpolado en x = "+str(valorInterpolado)+" es "+str(resultado))
            interpolacion.textValorX2.setText("")
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Digite correctamente el valor de x")
            msg.exec_()
            interpolacion.textValorX2.setText("")
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("No existen puntos agregados")
        msg.exec_()

def agregarPunto():
    try:
        x=float(interpolacion.textValorX.toPlainText())
        y=float(interpolacion.textValorY.toPlainText())
        Examen.valoresX.append(x)
        Examen.valoresY.append(y)
        interpolacion.textPuntos.setText("Valores de X : " + str(Examen.valoresX) + "\nValores de Y : " + str(Examen.valoresY))
        interpolacion.textValorX.setText("")
        interpolacion.textValorY.setText("")
    except ValueError:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("Ingrese correctamente el valor de x o y")
        msg.exec_()
        interpolacion.textValorX.setText("")
        interpolacion.textValorY.setText("")


def borrarinter():
    Examen.valoresX=[]
    Examen.valoresY=[]
    interpolacion.textPuntos.setText("Valores de X : "+str(Examen.valoresX)+"\nValores de Y : "+str(Examen.valoresY))


interpolacion.botonAgregar.clicked.connect(agregarPunto)
interpolacion.botonBorrar.clicked.connect(borrarinter)
interpolacion.botonResolver.clicked.connect(resolverinter)

interpolacion.show()
app.exec()