#crea una función que genera una lista de números en un intervalo dado y luego aplica otra función 
#a cada elemento de la lista, en python.
#TECNOLÓGICO NACIONAL DE MÉXICO Campus Jiquilpan
#Elaborado por: Flores Sánchez Ricardo
#Materia: Programación Lógica y Funcional
def Intervalo(funcion, inicio, fin, i=1):
    resultado = []
    valor = inicio
    while valor <= fin:
        resultado.append(funcion(valor))
        valor += i
    return resultado

def modulo(x):
    return x % 2

def potencia(y):
    return y ** 2

def suma(z):
    return z+(z-1)

resultado = Intervalo(modulo, 1, 10)
print(resultado)

resultado = Intervalo(potencia, 1, 10)
print(resultado)

resultado = Intervalo(suma, 1, 10)
print(resultado)