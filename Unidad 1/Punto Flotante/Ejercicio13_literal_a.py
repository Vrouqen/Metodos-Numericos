import struct
def num_ieee754_32bits(num):
    # Convierte el número a 32 bits (float) de coma flotante (IEEE 754)
    num1 = struct.pack('!f', num) #Contiene la secuencia de bytes '!f' para identificar el tipo de dato float

    # Convierte los bytes a una representación binaria
    numBinario = ''.join(format(byte, '08b') for byte in num1) # Recorre los bytes y los convierte a 8 bits
    # .join para concatenar los caracteres

    # Devuelve la representación binaria
    return numBinario

# Ejemplo de uso
numInf = 8
numInf_conversion = num_ieee754_32bits(numInf)
numSup = 9
numSup_conversion = num_ieee754_32bits(numSup)
print("8 a IEEE 754 32 bits: "+numInf_conversion)
print("9 a IEEE 754 32 bits: "+numSup_conversion)