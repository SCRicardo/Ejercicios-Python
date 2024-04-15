#Se ingresa por teclado la categoría de un socio de un club deportivo Sol Naciente y su antiguedad en años. Las 
#categorías posibles son A,B,C. Luego se desea saber si el socio ingresado tiene Categoría A o su antiguedad se encuentra 
#entre los 10 y 20 años, en esos casos, se pide mostrar un cartel que exprese lo siguiente "Socio VIP"
#TECNOLÓGICO NACIONAL DE MÉXICO Campus Jiquilpan
#Elaborado por: Flores Sánchez Ricardo
#Materia: Programación Lógica y Funcional
cat=input("Ingrese la categoría:")
ant=int(input("Ingrese su antiguedad:"))
if(cat=="A" ):
    print("Socio VIP")
else:
    if(ant>10 & ant<20):
        print("Socio VIP")
    else:
        print("Adelante")
