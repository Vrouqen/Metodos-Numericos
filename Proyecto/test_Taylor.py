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
        funcionStr=taylor.textFuncion.toPlainText()
        valorX=float(taylor.textValorX.toPlainText())
        nDerivadas=int(taylor.textNDerivadas.toPlainText())
        resultado=Unidad2.seriesDeTaylor(funcionStr,valorX,nDerivadas)
        print(resultado)
        taylor.labelResultado.setText("El resultado es : "+str(resultado))
        taylor.textValorX.setText("")
        
    except:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("Algún campo está mal digitado")
        msg.exec_()

taylor.botonResolver.clicked.connect(resolver)

taylor.show()
app.exec()