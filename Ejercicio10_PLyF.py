#Desarrolla un algoritmo que permita leer un valor cualquiera N y escriba si dicho numero es par o impar
#TECNOLÓGICO NACIONAL DE MÉXICO Campus Jiquilpan
#Elaborado por: Flores Sánchez Ricardo
#Materia: Programación Lógica y Funcional
print("Dame un número:")
num=int(input())
res=num%2
if(res==0):
    print("El número: ",num," es PAR")
else:
    print("El número: ",num," es IMPAR")