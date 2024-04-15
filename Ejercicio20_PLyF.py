#Solicitar al usuario que ingrese un número entero N,luego generar en forma aleatoria N números enteros comprendidos
#entre 1 y 100 y determinar cuántos pares y cuántos son impares
#TECNOLÓGICO NACIONAL DE MÉXICO Campus Jiquilpan
#Elaborado por: Flores Sánchez Ricardo
#Materia: Programación Lógica y Funcional
import random
num=int(input("Dame un número"))
pares = 0
impares = 0
for _ in range(num):
    numero = random.randint(1, 100)
    print(numero, end="   ")
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print()
print("Se generaron: ", pares, " números PAR")
print("Se generaron: ",impares," números IMPAR")