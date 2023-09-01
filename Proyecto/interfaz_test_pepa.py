import sys
from PySide2.QtCore import QPropertyAnimation
from PySide2 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from Proyecto.unidades.Unidad_1 import Unidad1
from Proyecto.unidades.Unidad_2 import Unidad2
from unidades.Examen import Examen
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
main.bt_siete.clicked.connect(lambda : main.stackedWidget.setCurrentWidget(main.page_taylor))
main.bt_ocho.clicked.connect(lambda : main.stackedWidget.setCurrentWidget(main.page_lagrange))
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

def convertirIEE754_32bits():
    if validadorDecimales(main.textNumero_2.toPlainText()):
        num=float(main.textNumero_2.toPlainText())
        convertido=Unidad1.convertirIEE754_32bits(num)
        main.labelNumTransformado_2.setText(str(convertido))
    else:
        main.textNumero.setText("")
def convertirIEE754_64bits():
    if validadorDecimales(main.textNumero_2.toPlainText()):
        num=float(main.textNumero_2.toPlainText())
        convertido=Unidad1.convertirIEE754_64bits(num)
        main.labelNumTransformado_2.setText(str(convertido))
    else:
        main.textNumero.setText("")

def calcularTeoremaBolzano():
    if validadorDecimales(main.textValorInf.toPlainText()) and validadorDecimales(main.textValorSup.toPlainText()):
        valorInf=float(main.textValorInf.toPlainText())
        valorSup=float(main.textValorSup.toPlainText())
        if valorInf < valorSup:
            funcion=main.textFuncion.toPlainText()
            respuesta=Unidad1.teoremaBolzano(valorInf,valorSup,funcion)
            if respuesta==True:
                main.labelResultado_3.setText("Existe una raíz en el intervalo dado")
            else:
                main.labelResultado_3.setText("No se encontró una raíz en el intervalo dado")
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Ingrese correctamente el intervalo")
            msg.exec_()
            main.textValorInf.setText("")
            main.textValorSup.setText("")
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("Ingrese correctamente los números")
        msg.exec_()
        main.textValorInf.setText("")
        main.textValorSup.setText("")

def mostrarGraficaFuncionBolzano():
    if validadorDecimales(main.textValorInf.toPlainText()) and validadorDecimales(main.textValorSup.toPlainText()):
        valorInf = float(main.textValorInf.toPlainText())
        valorSup = float(main.textValorSup.toPlainText())
        if valorInf < valorSup:
            funcion = main.textFuncion.toPlainText()
            Unidad1.graficarFuncion(valorInf,valorSup,funcion)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Ingrese correctamente el intervalo")
            msg.exec_()
            main.textValorInf.setText("")
            main.textValorSup.setText("")
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("Ingrese correctamente los números")
        msg.exec_()
        main.textValorInf.setText("")
        main.textValorSup.setText("")

def mostrarGraficaFuncionBiseccion():
    validarInf=validadorDecimales(main.textValorInf_2.toPlainText())
    validarSup=validadorDecimales(main.textEdit.toPlainText())
    if validarInf==True and validarSup==True:
        valorInf = float(main.textValorInf_2.toPlainText())
        valorSup = float(main.textEdit.toPlainText())
        if valorInf < valorSup:
            funcion = main.textFuncion_2.toPlainText()
            Unidad1.graficarFuncion(valorInf,valorSup,funcion)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Ingrese correctamente el intervalo")
            msg.exec_()
            main.textValorInf_2.setText("")
            main.textEdit.setText("")
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("Ingrese correctamente los números")
        msg.exec_()
        main.textValorInf_2.setText("")
        main.textEdit.setText("")

def calcularMétodoBisección():
    print(validadorDecimales(main.textValorInf_2.toPlainText()))
    print(validadorDecimales(main.textEdit.toPlainText()))
    if validadorDecimales(main.textValorInf_2.toPlainText()) and validadorDecimales(main.textEdit.toPlainText()):
        valorInf=float(main.textValorInf_2.toPlainText())
        valorSup=float(main.textEdit.toPlainText())
        if valorInf < valorSup:
            funcion=main.textFuncion_2.toPlainText()
            respuesta=Unidad1.metodoBiseccion(valorInf,valorSup,0.0001,funcion)
            main.labelResultado_4.setText("La raíz en el intervalo es "+str(respuesta))
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Ingrese correctamente el intervalo")
            msg.exec_()
            main.textValorInf_2.setText("")
            main.textValorSup_2.setText("")
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("Ingrese correctamente los números")
        msg.exec_()
        main.textValorInf_2.setText("")
        main.textEdit.setText("")

def ayuda():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setWindowTitle("Ayuda")
    msg.setText("Un ejemplo para insertar una ecuacion de buena forma es: (x**(3+2x))/x+3x**4")
    msg.exec_()
    main.textValorInf.setText("")
    main.textEdit.setText("")
def resolvertay():
    try:
        funcionStr = main.textFuncion_3.toPlainText()
        valorX = float(main.textValorX_2.toPlainText())
        nDerivadas = int(main.textNDerivadas.toPlainText())
        resultado = Unidad2.seriesDeTaylor(funcionStr, valorX, nDerivadas)
        print(resultado)
        main.labelResultado_5.setText("El resultado es : " + str(resultado))
        main.textValorX_2.setText("")

    except:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("Algún campo está mal digitado")
        msg.exec_()

def resolverinter():
    if len(Examen.valoresX)!=0 and len(Examen.valoresY)!=0:
        try:
            valorX=float(main.textValorX2.toPlainText())
            valoresX=Examen.valoresX
            valoresY=Examen.valoresY
            funcionInterpolada = Examen.interpolacionPolinomicaLagrange(valoresX, valoresY)
            valorInterpolado = valorX
            resultado = funcionInterpolada(valorInterpolado)
            main.labelResultado_6.setText("El valor interpolado en x = "+str(valorInterpolado)+" es "+str(resultado))
            main.textValorX2.setText("")
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Digite correctamente el valor de x")
            msg.exec_()
            main.textValorX2.setText("")
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("No existen puntos agregados")
        msg.exec_()

def agregarPunto():
    try:
        x=float(main.textValorX_3.toPlainText())
        y=float(main.textValorY.toPlainText())
        Examen.valoresX.append(x)
        Examen.valoresY.append(y)
        main.textPuntos.setText("Valores de X : " + str(Examen.valoresX) + "\nValores de Y : " + str(Examen.valoresY))
        main.textValorX_3.setText("")
        main.textValorY.setText("")
    except ValueError:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("Ingrese correctamente el valor de x o y")
        msg.exec_()
        main.textValorX_3.setText("")
        main.textValorY.setText("")


def borrarinter():
    Examen.valoresX=[]
    Examen.valoresY=[]
    main.textPuntos.setText("Valores de X : "+str(Examen.valoresX)+"\nValores de Y : "+str(Examen.valoresY))


#Asignación de funciones/utilidades
main.botonAbs.clicked.connect(calcularErrorAbs) #Calcular Error Absoluto
main.botonRelat.clicked.connect(calcularErrorRelativo) #Calcular Error Relativo

main.botonCalcular.clicked.connect(solucionDeEcuacion)#Solución de la ecuación (e^x)/(e^x -1)
main.botonGrafico.clicked.connect(mostraGraficaPropagacionErrores)#Grafica de la funcion

main.boton32bits.clicked.connect(convertirIEE754_32bits)#Conversion de numero a IEE 754 32 bits
main.boton64bits.clicked.connect(convertirIEE754_64bits)#Conversion de numero a IEE 754 64 bits

main.botonCalcular_2.clicked.connect(calcularTeoremaBolzano)#Calcula el Teorema de bolzano
main.botonGrafico_2.clicked.connect(mostrarGraficaFuncionBolzano)#Grafica del Teoreama de bolzano
main.botonAyuda.clicked.connect(ayuda)#Boton de ayuda para ingresar la función

main.botonCalcular_3.clicked.connect(calcularMétodoBisección)#Calcula el método de Bisección
main.botonGrafico_3.clicked.connect(mostrarGraficaFuncionBiseccion)#Grafica del método de Bisección
main.botonAyuda_2.clicked.connect(ayuda)#Boton de ayuda para ingresar la función

main.botonResolver.clicked.connect(resolvertay)

main.botonAgregar.clicked.connect(agregarPunto)
main.botonBorrar.clicked.connect(borrarinter)
main.botonResolver_2.clicked.connect(resolverinter)

main.show()
app.exec()