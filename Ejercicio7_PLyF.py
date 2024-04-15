#Realiza un algoritmo que permita calcular el área y volumen de un cilindro dado su radio y su altura, mostrar en pantalla
#TECNOLÓGICO NACIONAL DE MÉXICO Campus Jiquilpan
#Elaborado por: Flores Sánchez Ricardo
#Materia: Programación Lógica y Funcional
print("Dame el radio:")
radio=float(input())
print("Dame la altura:")
altura=float(input())
PI=3.14
volumen=PI*(radio*radio)*altura
area=(2*PI*radio*altura)+(2*PI*(radio*radio))
print("El volumen del cilindro es de: ",volumen)
print("El área del cilindro es de: ",area)