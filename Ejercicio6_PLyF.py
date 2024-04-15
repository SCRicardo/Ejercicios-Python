#A un trabajador le pagan sus horas laborales, si la cantidad de horas trabajadas es mayor a 40, la tarifa se incrementa
#en 50% para las horas extras, calcular el salario del trabajador dadas sus horas trabajadas y la tarifa por hora.
#TECNOLÓGICO NACIONAL DE MÉXICO Campus Jiquilpan
#Elaborado por: Flores Sánchez Ricardo
#Materia: Programación Lógica y Funcional
print("Dame las horas trabajadas:")
horas=int(input())
print("Ingresa la tarifa por hora:")
tarifa=float(input())
resta=horas-40
horas=horas-resta
if(resta>0):
    tarifaTotal=(horas*tarifa)+(resta*(tarifa*1.5))
    print("La tarifa total es de: ",tarifaTotal)
else:
    horas=horas+resta
    tarifaTotal=horas*tarifa
    print("La tarifa total es de: ",tarifaTotal)