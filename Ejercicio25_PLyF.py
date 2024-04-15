#Desarrollar un algoritmo que permita convertir calificaciones numéricas, según la siguiente tabla:
#A=20,19  B=18,17,16  C=15,14,13  D=12,11,10 E=1-9 . La nota se encuentra entre 1 y 20.
#TECNOLÓGICO NACIONAL DE MÉXICO Campus Jiquilpan
#Elaborado por: Flores Sánchez Ricardo
#Materia: Programación Lógica y Funcional
nota=int(input("Ingrese la nota: "))
if(nota==20):
    print("Tu nota es A.")
if(nota==19):
    print("Tu nota es A.")
if(nota==18):
    print("Tu nota es B.")
if(nota==17):
    print("Tu nota es B.")
if(nota==16):
    print("Tu nota es B.")
if(nota==15):
    print("Tu nota es C.")
if(nota==14):
    print("Tu nota es C.")
if(nota==13):
    print("Tu nota es C.")
if(nota==12):
    print("Tu nota es D.")
if(nota==11):
    print("Tu nota es D.")
if(nota==10):
    print("Tu nota es D.")
if(nota>1):
    if(nota<9):
        print("Tu nota es E.")