#Realizar un algoritmo que permita Sumar, Restar, Multiplicar o Dividir dos numeros
#TECNOLÓGICO NACIONAL DE MÉXICO Campus Jiquilpan
#Elaborado por: Flores Sánchez Ricardo
#Materia: Programación Lógica y Funcional
n1=2
n2=2
op=0
print("Dame la opción")
print("1.- Suma")
print("2.- Resta")
print("3.- Multiplicación")
print("4.- División")
op = int(input()) 
if(op==1) :
    r=n1+n2
    print("La suma es: ",r)
elif(op==2):
    r=n1-n2
    print("La resta es: ",r)
elif(op==3):
    r=n1*n2
    print("La multiplicación es: ",r)
elif(op==4):
    r=n1/n2
    print("La división es: ",r)