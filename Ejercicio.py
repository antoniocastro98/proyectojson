from Funciones import listar, contar, buscar, info
import json
with open ("archivojson.json") as fichero:
    datos=json.load(fichero)



print(''' MENU
1.Listar información: Mostrar el nombre de las cines de los que tenemos información.

2.Contar información: Mostrar los cines y la cantidad de peliculas que proyectan.

3.Buscar o filtrar información: Pedir por teclado un nombre de un cine y mostramos la dirección y donde se encuentra.

4.Buscar información relacionada: Introducir una sesión y mostrar los cines que proyectan peliculas en esas sesiones.

5.Ejercicio libre: Introducir una hora y mostrar las peliculas que se proyectan.''')

opcion=int(input("Introduce una opción: "))

while opcion<0 or opcion>5:
    print ("Error, introduce una opción correcta")
    opcion=int(input("Introduce una opción: "))

while opcion!=0:
    if opcion==1:
        for i in listar(datos):
            print (i)
        opcion=int(input("Introduce una opción: "))
        while opcion<0 or opcion>5:
            print ("Error, introduce una opción correcta")
            opcion=int(input("Introduce una opción: "))
    if opcion==2:
        for i in contar(datos):
            for x in i:
                print(x)
        opcion=int(input("Introduce una opción: "))
        while opcion<0 or opcion>5:
            print ("Error, introduce una opción correcta")
            opcion=int(input("Introduce una opción: "))
    if opcion==3:
        nombre=input("Introduce el nombre del cine: ")
        for i in buscar(datos,nombre):
            print(i)
        if len(buscar(datos,nombre))==0:
            print("Error, el cine no aparece")
        opcion=int(input("Introduce una opción: "))
        while opcion<0 or opcion>5:
            print ("Error, introduce una opción correcta")
            opcion=int(input("Introduce una opción: "))
    if opcion==4:
        sesion=input("Introduce el nombre de una sesión (de uno a siete en letras): ")
        for i in info(datos,sesion):
            print(i)
        if len(buscar(datos,sesion))==0:
            print("Error, la sesión no existe")
        opcion=int(input("Introduce una opción: "))
        while opcion<0 or opcion>5:
            print ("Error, introduce una opción correcta")
            opcion=int(input("Introduce una opción: "))
    if opcion==5:
        
        opcion=int(input("Introduce una opción: "))
        while opcion<0 or opcion>5:
            print ("Error, introduce una opción correcta")
            opcion=int(input("Introduce una opción: "))


if opcion==0:
    print("Fin del programa")