#Se generan números enteros en forma aleatoria entre 0 y 200 hasta que la sumatoria de los números sea mayor a 500.
#Al finalizar indicar:
#a)La cantidad de números nulos (0)
#b)La sumatoria de los números que se encuentran entre el 10 y 100
#c)El promedio de los números menores a 150
#d)El número mayor generado
#TECNOLÓGICO NACIONAL DE MÉXICO Campus Jiquilpan
#Elaborado por: Flores Sánchez Ricardo
#Materia: Programación Lógica y Funcional
import random;
cero=0
suma1=0
suma2=0
suma3=0
mayor=0
cont=0
while(suma1<500):
    num=random.randint(0, 200)
    suma1+=num
    if(num==0):
        cero+=1
    if(num>10):
        if(num<100):
            suma2+=num
    if(num<150):
        cont+=1
        suma3+=num
    if(num>mayor):
        mayor=num
prom=suma3/cont if cont > 0 else 0
print("La cantidad de números nulos (0) es de: ",cero)
print("La suma total es de: ",suma1)
print("La suma e los números entre 1 y 100 es de: ",suma2)
print("El promedio de los números menores a 150 es de: ",prom)
print("El número mayor generado es: ",mayor)