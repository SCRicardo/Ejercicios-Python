#Determinar un algoritmo que permita leer un valor entero positivo y determinar si es primo o no.
#TECNOLÓGICO NACIONAL DE MÉXICO Campus Jiquilpan
#Elaborado por: Flores Sánchez Ricardo
#Materia: Programación Lógica y Funcional
num=int(input("Dame un número:"))
i=2
while(i<num):
    if(i+1==num):
        print("Es PRIMO")
    res=num%i
    if(res==0):
        print("No es PRIMO")
        break
    else:
        i+=1

    