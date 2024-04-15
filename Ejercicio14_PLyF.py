#Desarrollar un algoritmo que te permita leer un valor n y describa si es número par o impar
#TECNOLÓGICO NACIONAL DE MÉXICO Campus Jiquilpan
#Elaborado por: Flores Sánchez Ricardo
#Materia: Programación Lógica y Funcional
num=int(input("Dame un valor numérico:"))
res=num%2
if(res==0):
    print("El número es PAR")
else:
    print("El número es IMPAR")