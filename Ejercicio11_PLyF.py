#Realizar un algoritmo que lea 10 numeros y los ordene de mayor a menor y mostrarlo
#TECNOLÓGICO NACIONAL DE MÉXICO Campus Jiquilpan
#Elaborado por: Flores Sánchez Ricardo
#Materia: Programación Lógica y Funcional
a=[]
for i in range(10):
    valor=int(input("Ingresa el número: "))
    a.append(valor)

a.sort(reverse=True)
print(a)