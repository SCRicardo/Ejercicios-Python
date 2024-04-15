#Ingresa un número entero para saber si es divisible por 7 y es mayor a 40
#TECNOLÓGICO NACIONAL DE MÉXICO Campus Jiquilpan
#Elaborado por: Flores Sánchez Ricardo
#Materia: Programación Lógica y Funcional
num=int(input("Dame un número:"))
if(num>40):
    res=num%7
    if(res==0):
        print("Número correcto")
    else:
        print("Número incorrecto")
else:
    print("El número no es mayor a 40")