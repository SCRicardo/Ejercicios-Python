#Determinar la hipotenusa de un triángulo rectángulo conociendo las longitudes de sus dos catetos.
#TECNOLÓGICO NACIONAL DE MÉXICO Campus Jiquilpan
#Elaborado por: Flores Sánchez Ricardo
#Materia: Programación Lógica y Funcional
import math
c1=float(input("Cateto 1:"))
c2=float(input("Cateto 2:"))
h=math.sqrt(c1**2+c2**2)
print("La hipotenusa de un triángulo rectángulo es: ",h)