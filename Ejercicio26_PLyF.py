#Desarrollar un algoritmo para la empresa Constructora TecnoVivir Casas C.A., que le permite calcular e imprimir 
#la nómina para su cancelación a un total de 50 obreros calificados a quienes debe cancelar por horas trabajadas.
#La hora trabajada se pautó en 30 000 Bolívares
#TECNOLÓGICO NACIONAL DE MÉXICO Campus Jiquilpan
#Elaborado por: Flores Sánchez Ricardo
#Materia: Programación Lógica y Funcional
trabajadores=50
pago=30000
op=0
cont=1

while(cont<=trabajadores):
    horaTrabajada=input("Hora trabajada: ")
    op=int(horaTrabajada) * pago
    print("Su salario es de: ", op)
    cont=cont + 1

print("Fin del algortimo, gracias")