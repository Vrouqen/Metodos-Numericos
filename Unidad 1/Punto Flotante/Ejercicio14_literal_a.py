import struct
def num_ieee754_64bits(num):
    num1 = struct.pack('!d', num) #Contiene la secuencia de bytes
    # Convierte el número a 64 bits (double) de coma flotante (IEEE 754)

    # Convierte los bytes a una representación binaria
    numBinario = ''.join(format(byte, '08b') for byte in num1) # Recorre los bytes y los convierte a 8 bits
    # .join para concatenar los caracteres

    # Devuelve la representación binaria
    return numBinario

# Ejemplo de uso
numero_decimal = 17.25
conversion_binario = num_ieee754_64bits(numero_decimal)
print(conversion_binario)