#Leer 3 números por teclado y designar cuál es el mayor de ellos, además de verificar cuál es el menor de ellos.
#TECNOLÓGICO NACIONAL DE MÉXICO Campus Jiquilpan
#Elaborado por: Flores Sánchez Ricardo
#Materia: Programación Lógica y Funcional
print("Dame numero 1:")
n1=int(input())
print("Dame numero 2:")
n2=int(input())
print("Dame numero 3:")
n3=int(input())
mayor=n1
menor=n1
if(n2>=mayor):
    mayor=n2
else:
    menor=n2
if(n3>=mayor):
    mayor=n3
    print("El mayor es: ",mayor)
    print("El menor es: ",menor)
else:
    menor=n3
    if(n2<=menor):
        menor=n2
    elif(n1<=menor):
        menor=n1
        print("El mayor es: ",mayor)
        print("El menor es: ",menor)

