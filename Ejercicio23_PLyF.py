#Se leen desde teclado números hasta que la suma de los mismos llegue a 1000. Mientras tanto debe de hallar:
#a)La cantidad de números múltiplos de 6
#b)La suma de los números que se encuentran entre el 1 y 10.
#TECNOLÓGICO NACIONAL DE MÉXICO Campus Jiquilpan
#Elaborado por: Flores Sánchez Ricardo
#Materia: Programación Lógica y Funcional
suma=0
cont=0
contNum=0
while(suma<1000):
    num=int(input("Dame un número: "))
    suma+=num
    mod=num%6
    if(mod==0):
        cont+=1
    if(num>1):
        if(num<10):
            contNum=contNum+num
    print("Número registrado")
print("La suma de los números es de: ",suma)
print("La cantidad de números múltiplos de 6 son: ",cont)
print("La suma de los números entre 1 y 10 son: ",contNum)