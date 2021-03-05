from lxml import etree
from Funciones import listar, contar
datos=etree.parse("archivoxml.xml")

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
            print (i)
        opcion=int(input("Introduce una opción: "))
        while opcion<0 or opcion>5:
            print ("Error, introduce una opción correcta")
            opcion=int(input("Introduce una opción: "))
    if opcion==3:
        for i in contar(datos):
            print (i)
        opcion=int(input("Introduce una opción: "))
        while opcion<0 or opcion>5:
            print ("Error, introduce una opción correcta")
            opcion=int(input("Introduce una opción: "))
    if opcion==4:
        for i in contar(datos):
            print (i)
        opcion=int(input("Introduce una opción: "))
        while opcion<0 or opcion>5:
            print ("Error, introduce una opción correcta")
            opcion=int(input("Introduce una opción: "))
    if opcion==5:
        for i in contar(datos):
            print
        opcion=int(input("Introduce una opción: "))
        while opcion<0 or opcion>5:
            print ("Error, introduce una opción correcta")
            opcion=int(input("Introduce una opción: "))


if opcion==0:
    print("Fin del programa")