from datetime import datetime
class ManejoArchivos:
    def almacenarDatosErrores(tipoError,valorReal, valorAproximado, resultado, nombre_archivo):
        # Esta función almacena los datos en un archivo
        with open(nombre_archivo, 'a') as archivo:
            archivo.write("FechaGenerado: {}\n".format(datetime.now()))
            archivo.write("ValorReal: {}\n".format(valorReal))
            archivo.write("ValorAproximado: {}\n".format(valorAproximado))
            if tipoError==1: #Almacena absolutos colocando 1 en el método
                archivo.write("ErrorAbsoluto: {}\n".format(resultado))
            elif tipoError==2: #Almacena relativos colocando 1 en el método
                archivo.write("ErrorRelativo: {}\n".format(resultado))
            archivo.write("\n")  # Agregar una línea en blanco para separar los datos de distintos usuarios


