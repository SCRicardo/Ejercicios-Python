#Se ingresa por teclado los catetos de un triángulo rectángulo. Se desea hallar y mostrar su hipotenusa
#TECNOLÓGICO NACIONAL DE MÉXICO Campus Jiquilpan
#Elaborado por: Flores Sánchez Ricardo
#Materia: Programación Lógica y Funcional
import math
c1=int(input("Cateto 1:"))
c2=int(input("Cateto 2:"))
h=math.sqrt(c1**2+c2**2)
print("La hipotenusa es: ",h)