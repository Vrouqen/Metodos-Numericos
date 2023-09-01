from datetime import datetime
from reportlab.pdfgen import canvas
from fpdf import FPDF
import os

class ManejoArchivos:
    def convertirTxtToPDF(input_file,output_file):
        # Verificar si el archivo de entrada existe
        if not os.path.isfile(input_file):
            return "El archivo de entrada no existe."

        # Leer el contenido del archivo de texto
        with open(input_file, "r", encoding="utf-8") as txt_file:
            text_content = txt_file.read()

        # Crear el archivo PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=text_content)

        # Guardar el archivo PDF
        pdf.output(output_file)

        return "Archivo PDF generado exitosamente."

    def almacenarDatosErrores(tipoError,valorReal, valorAproximado, resultado):
        # Esta función almacena los datos en un archivo
        with open("archivos\Errores.txt", 'a') as archivo:
            archivo.write("FechaGenerado: {}\n".format(datetime.now()))
            archivo.write("ValorReal: {}\n".format(valorReal))
            archivo.write("ValorAproximado: {}\n".format(valorAproximado))
            if tipoError==1: #Almacena absolutos colocando 1 en el método
                archivo.write("ErrorAbsoluto: {}\n".format(resultado))
            elif tipoError==2: #Almacena relativos colocando 1 en el método
                archivo.write("ErrorRelativo: {}\n".format(resultado))
            archivo.write("\n")  # Agregar una línea en blanco para separar los datos de distintos usuarios

    def almacenarDatosSistemasNumeracion(tipoTransformacion,numOriginal,numTransformado):
        # Esta función almacena los datos en un archivo
        with open("archivos\SistemasNumeracion.txt", 'a') as archivo:
            archivo.write("FechaGenerado: {}\n".format(datetime.now()))
            if tipoTransformacion==1:
                archivo.write("NumeroBinario: {}\n".format(numOriginal))
                archivo.write("NumeroDecimal: {}\n".format(numTransformado))
            elif tipoTransformacion==2:
                archivo.write("NumeroDecimal: {}\n".format(numOriginal))
                archivo.write("NumeroBinario: {}\n".format(numTransformado))
            elif tipoTransformacion==3:
                archivo.write("NumeroHexadecimal: {}\n".format(numOriginal))
                archivo.write("NumeroDecimal: {}\n".format(numTransformado))
            elif tipoTransformacion==4:
                archivo.write("NumeroOctal: {}\n".format(numOriginal))
                archivo.write("NumeroDecimal: {}\n".format(numTransformado))
            archivo.write("\n")  # Agregar una línea en blanco para separar los datos de distintos usuarios

    def almacenarDatosIEE(tipoTransformacion, numOriginal, numTransformado):
        with open("archivos\IEEE.txt", 'a') as archivo:
            archivo.write("FechaGenerado: {}\n".format(datetime.now()))
            if tipoTransformacion==1:
                archivo.write("NumeroDecimal: {}\n".format(numOriginal))
                archivo.write("Numero32bits: {}\n".format(numTransformado))
            elif tipoTransformacion==2:
                archivo.write("NumeroDecimal: {}\n".format(numOriginal))
                archivo.write("Numero64bits: {}\n".format(numTransformado))
            archivo.write("\n")  # Agregar una línea en blanco para separar los datos de distintos usuarios

    def almacenarDatosPropagacion(valorx,valory):
        with open("archivos\PropagacionErrores.txt", 'a') as archivo:
            archivo.write("FechaGenerado: {}\n".format(datetime.now()))
            archivo.write("Valorx: {}\n".format(valorx))
            archivo.write("Valory: {}\n".format(valory))
            archivo.write("\n")  # Agregar una línea en blanco para separar los datos de distintos usuarios

    def almacenarDatosBolzano(valorInf, valorSup, funcion,raiz):
        with open("archivos\TeoremaBolzano.txt", 'a') as archivo:
            archivo.write("FechaGenerado: {}\n".format(datetime.now()))
            archivo.write("Funcion: {}\n".format(funcion))
            archivo.write("ValorInferior: {}\n".format(valorInf))
            archivo.write("ValorSuperior: {}\n".format(valorSup))
            archivo.write("Raiz: {}\n".format(raiz))
            archivo.write("\n")  # Agregar una línea en blanco para separar los datos de distintos usuarios

    def almacenarDatosBiseccion(valorInf, valorSup, funcion,raiz):
        with open("archivos\MetodoBiseccion.txt", 'a') as archivo:
            archivo.write("FechaGenerado: {}\n".format(datetime.now()))
            archivo.write("Funcion: {}\n".format(funcion))
            archivo.write("ValorInferior: {}\n".format(valorInf))
            archivo.write("ValorSuperior: {}\n".format(valorSup))
            archivo.write("Raiz: {}\n".format(raiz))
            archivo.write("\n")  # Agregar una línea en blanco para separar los datos de distintos usuarios

    def almacenarDatosTaylor(funcion, valorX, nDerivadas):
        with open("archivos\SeriesTaylor.txt", 'a') as archivo:
            archivo.write("FechaGenerado: {}\n".format(datetime.now()))
            archivo.write("Funcion: {}\n".format(funcion))
            archivo.write("ValorX: {}\n".format(valorX))
            archivo.write("nDerivadas: {}\n".format(nDerivadas))
            archivo.write("\n")  # Agregar una línea en blanco para separar los datos de distintos usuarios

    def almacenarDatosLagrange(valoresX, valoresY,valorX):
        with open("archivos\SeriesLagrange.txt", 'a') as archivo:
            archivo.write("FechaGenerado: {}\n".format(datetime.now()))
            archivo.write("ValoresX: {}\n".format(valoresX))
            archivo.write("ValoresY: {}\n".format(valoresY))
            archivo.write("ValorX: {}\n".format(valorX))
            archivo.write("\n")  # Agregar una línea en blanco para separar los datos de distintos usuarios
