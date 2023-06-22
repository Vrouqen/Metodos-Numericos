from Unidad_1 import Unidad1
def opcion1():
    while True:
        print()
        print("1. Calcular error absoluto")
        print("2. Calcular error relativo")
        print("0. Regresar")
        seleccion = input("Selecciona una opción > ")
        if seleccion=="1":
            varReal=float(input("Ingrese el valor real > "))
            varAprox=float(input("Ingrese el valor aproximado > "))
            errorAbs=Unidad1.calcularErrorAbsoluto(varReal,varAprox)
            print("El error absoluto es: "+str(errorAbs))
        elif seleccion=="2":
            varReal=float(input("Ingrese el valor real > "))
            varAprox=float(input("Ingrese el valor aproximado > "))
            errorRel=Unidad1.calcularErrorRelativo(varReal,varAprox)
            print("El error relativo es: "+str(errorRel))
        elif seleccion=="0":
          break
        else:
            print("Opción inválida")

def opcion2():
    while True:
        print()
        print("1. Binario a decimal")
        print("2. Decimal a binario")
        print("3. Hexadecimal a decimal")
        print("4. Octal a decimal")
        print("0. Regresar")
        seleccion = input("Selecciona una opción > ")
        if seleccion=="1":
            binario=input("Ingrese el número binario > ")
            decimal=Unidad1.convertirBinarioToDecimal(binario)
            print("El valor en decimal es -> "+str(decimal))
        elif seleccion=="2":
            decimal=float(input("Ingrese el número decimal >"))
            binario=Unidad1.convertirDecimalToBinario(decimal)
            print("El valor en binario es -> "+str(binario))
        elif seleccion=="3":
            #Falta validar los caracteres
            hexadecimal=input("Ingrese el número hexadecimal > ")
            decimal=Unidad1.convertirHexadecimalToDecimal(hexadecimal)
            print("El valor en decimal es -> "+str(decimal))
        elif seleccion=="4":
            #Falta validar los caracteres
            octal=int(input("Ingrese el número octal > "))
            decimal=Unidad1.convertirOctalToDecimal(octal)
            print("El valor en decimal es -> "+str(decimal))
        elif seleccion=="0":
          break
        else:
            print("Opción inválida")

def opcion3():
    while True:
        print()
        print("1. Transformar decimal al formato IEEE 754 de 32 bits")
        print("2. Transformar decimal al formato IEEE 754 de 64 bits")
        print("0. Regresar")
        seleccion = input("Selecciona una opción > ")
        if seleccion=="1":
            numDecimal=float(input("Ingrese el número a transformar > "))
            numIEEE32=Unidad1.convertirIEE754_32bits(numDecimal)
            print("El número transformado es -> "+str(numIEEE32))
        elif seleccion=="2":
            numDecimal=float(input("Ingrese el número a transformar > "))
            numIEEE64=Unidad1.convertirIEE754_64bits(numDecimal)
            print("El número transformado es -> "+str(numIEEE64))
        elif seleccion=="0":
          break
        else:
            print("Opción inválida")

def opcion4():
  while True:
        print()
        print("1. Calcular el f(x)=(e^x)/(e^x -1) para valores mayores a 250")
        print("2. Mostrar el comportamiento de la gráfica")
        print("0. Regresar")
        seleccion = input("Selecciona una opción > ")
        if seleccion=="1":
            num=float(input("Ingrese el valor de x > "))
            respuesta=Unidad1.solucionDeEcuacion(num)
            print("El resultado de la ecuación es -> "+str(respuesta))
        elif seleccion=="2":
            max=float(input("Ingrese hata que valor de x será la gráfica > "))
            if max>1:
                Unidad1.graficaDeEcuacion(max)
            else:
                print("No se admiten valores menores que uno")
        elif seleccion=="0":
          break
        else:
            print("Opción inválida")

# Función para mostrar el menú y obtener la selección del usuario
def mostrar_menu():
    print("======= MENÚ =======")
    print("1. Calculo de errores")
    print("2. Sistemas de numeración")
    print("3. Punto flotante")
    print("4. Propagacion de errores")
    print("5. Teorema de Bolzano")
    print("6. Método de Bisección")
    print("0. Salir")
    print("====================")
    seleccion = input("Selecciona una opción: ")
    return seleccion

# Función principal del programa
def main():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            opcion1()
        elif opcion == "2":
            opcion2()
        elif opcion == "3":
            opcion3()
        elif opcion == "4":
            opcion4()
        elif opcion == "5":
            print()
        elif opcion == "6":
            print()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

# Llamada a la función principal
main()
