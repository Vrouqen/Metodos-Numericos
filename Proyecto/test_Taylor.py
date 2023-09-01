import sys
from PySide2.QtCore import QPropertyAnimation
from PySide2 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from Proyecto.unidades.Unidad_2 import Unidad2
import math
from unidades.Examen import Examen

#Iniciar la aplicación
app=QtWidgets.QApplication([])
taylor=uic.loadUi("interfaz\SeriesTaylor.ui")


def resolver():
    try:
        valorX=float(taylor.textValorX.toPlainText())
        try:
            nDerivadas=int(taylor.textNDerivadas.toPlainText())
            try:
                funcionStr=taylor.textFuncion.toPlainText()
                resultado=Unidad2.calcularSeriesTaylor(funcionStr,0,valorX,nDerivadas)
                print(resultado)
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Error")
                msg.setText("Ingrese correctamente la función")
                msg.exec_()
        except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Error")
                msg.setText("Ingrese correctamente la\ncantidad de derivadas")
                msg.exec_()
                taylor.textNDerivadas.setText("")
    except:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("Ingrese correctamente el valor de x ")
        msg.exec_()
        taylor.textValorX.setText("")

taylor.botonResolver.clicked.connect(resolver)

taylor.show()
app.exec()