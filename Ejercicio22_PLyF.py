#Diseñar un algoritmo que lea desde teclado la información sobre altura, edad y sexo (M/F) de los participantes de 
#un concurso. La lectura finaliza cuando se lee un valor de altura negativo. Luego calcule:
#a)Promedio de altura de mujeres
#b)Promedio de altura de hombres
#c)Promedio de edad de los participantes
#TECNOLÓGICO NACIONAL DE MÉXICO Campus Jiquilpan
#Elaborado por: Flores Sánchez Ricardo
#Materia: Programación Lógica y Funcional
altF=0
altM=0
edadP=0
aux1=0
aux2=0
aux3=0
while True:
    altura=int(input("Dame la altura en cm:"))
    if altura<0:
        break
    edad=int(input("Dame la edad:"))
    sexo=input("Dame el sexo (M/F):")
    if(sexo=="F"):
        altF+=altura
        aux1+=1
        edadP+=edad
        aux3+=1
    elif(sexo=="M"):
        altM+=altura
        aux2+=1
        edadP+=edad
        aux3+=1
r1=altF/aux1
r2=altM/aux2
r3=edadP/aux3
print("Promedio de altura de mujeres: ",r1)
print("Promedio de altura de hombres: ",r2)
print("Promedio de altura de los participantes: ",r3)