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
def botonErorres():
    calcErrores.show()


main.bt_uno.clicked.connect(lambda : main.stackedWidget.setCurrentWidget(main.page))
main.bt_dos.clicked.connect(lambda : main.stackedWidget.setCurrentWidget(main.page_uno))
main.bt_tres.clicked.connect(lambda : main.stackedWidget.setCurrentWidget(main.page_dos))
main.bt_cuatro.clicked.connect(lambda : main.stackedWidget.setCurrentWidget(main.page_tres))
main.bt_cinco.clicked.connect(lambda : main.stackedWidget.setCurrentWidget(main.page_cuatro))
main.bt_seis.clicked.connect(lambda : main.stackedWidget.setCurrentWidget(main.page_cinco))

main.show()
app.exec()