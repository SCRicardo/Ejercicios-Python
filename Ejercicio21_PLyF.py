#El factorial de un número entero se denota de la siguiente manera n! y su resultado es n!=n*(n-1)*(n-2)...1
#Por ejemplo, 5!=5*4*3*2*1 siendo el resultado 120. Leer un valor N y determine su factorial
#TECNOLÓGICO NACIONAL DE MÉXICO Campus Jiquilpan
#Elaborado por: Flores Sánchez Ricardo
#Materia: Programación Lógica y Funcional
num=int(input("Dame un número:"))
aux=num
while(num>1):
    aux=aux*(num-1)
    num-=1
print("El factorial es: ",aux)