#Dada la calificación de un alumno, mostrar en pantalla si es aprobado siempre y cuando tenga el 80% de asistencia,
#y su calificación, en caso de no contar con el 80% se muestre como reprobado.
#TECNOLÓGICO NACIONAL DE MÉXICO Campus Jiquilpan
#Elaborado por: Flores Sánchez Ricardo
#Materia: Programación Lógica y Funcional
print("Ingresa la calificación: ")
calif=int(input())
print("Ingresa porcentaje (%) de asistencia:")
asistencia=int(input())
if(asistencia>=80 & calif>69):
    print("Aprobado con: ",calif)
else:
    print("Reprobado")