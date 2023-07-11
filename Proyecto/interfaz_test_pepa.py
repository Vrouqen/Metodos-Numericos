import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from Unidad_1 import Unidad1
import matplotlib.pyplot as plt #Gráficos
#Iniciar la aplicación
app=QtWidgets.QApplication([])
main=uic.loadUi("interfaz/ventana_principal.ui")
calcErrores=uic.loadUi("CalculoErrores.ui")
def cerrar():
    main.close()
def botonErorres():
    calcErrores.show()

main.bt_cerrar.clicked.connect(cerrar)#Sale del programa
main.bt_uno.clicked.connect(botonErorres)#Sale del programa

main.show()
app.exec()