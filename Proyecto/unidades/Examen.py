from Proyecto.unidades.Archivos import ManejoArchivos

class Examen:
    #nterpolación polinómica lagrange
    valoresX=[]
    valoresY=[]
    def interpolacionPolinomicaLagrange(valoresX, valoresY):
        def interpolate(x):
            n = len(valoresX)
            valorInterpolado = 0.0
            for i in range(n):
                termino = valoresY[i]
                for j in range(n):
                    if i != j:
                        termino *= (x - valoresX[j]) / (valoresX[i] - valoresX[j])
                valorInterpolado += termino
            return valorInterpolado
        ManejoArchivos.almacenarDatosLagrange(valoresX,valoresY,x)
        return interpolate


