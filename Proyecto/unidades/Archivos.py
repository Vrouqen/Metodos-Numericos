from datetime import datetime
class ManejoArchivos:
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
            if tipoTransformacion==1:
                archivo.write("NumeroDecimal: {}\n".format(numOriginal))
                archivo.write("Numero32bits: {}\n".format(numTransformado))
            elif tipoTransformacion==2:
                archivo.write("NumeroDecimal: {}\n".format(numOriginal))
                archivo.write("Numero64bits: {}\n".format(numTransformado))
            archivo.write("\n")  # Agregar una línea en blanco para separar los datos de distintos usuarios