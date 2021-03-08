import json 
with open ("archivojson.json") as fichero:
    datos=json.load(fichero)

def listar (datos):
    lista=[]
    i=datos.get("cines").get("cinecallao").get("nombre")
    lista.append(i)
    a=datos.get("cines").get("cinesaparquesur").get("nombre")
    lista.append(a)
    e=datos.get("cines").get("cinesaprincipepio").get("nombre")
    lista.append(e)
    o=datos.get("cines").get("yelmoalcorcon").get("nombre")
    lista.append(o)
    return lista

def contar (datos):
    lista=[]
    lista2=[]
    lista3=[]
    i=datos.get("cines").get("cinecallao").get("nombre")
    lista2.append(i)
    i2=datos.get("cines").get("cinecallao").get("peliculas")
    lista2.append(i2)
    a=datos.get("cines").get("cinesaparquesur").get("nombre")
    lista2.append(a)
    a2=datos.get("cines").get("cinesaparquesur").get("peliculas")
    lista2.append(a2)
    e=datos.get("cines").get("cinesaprincipepio").get("nombre")
    lista2.append(e)
    e2=datos.get("cines").get("cinesaprincipepio").get("peliculas")
    lista2.append(e2)
    o=datos.get("cines").get("yelmoalcorcon").get("nombre")
    lista2.append(o)
    o2=datos.get("cines").get("yelmoalcorcon").get("peliculas")
    lista2.append(o2)
    lista.append(lista2)
    return lista

def buscar (datos,nombre):
    lista=[]
    if nombre==datos.get("cines").get("cinecallao").get("nombre"):
        lista.append(datos.get("cines").get("cinecallao").get("direccion"))
        lista.append(datos.get("cines").get("cinecallao").get("encuentra"))
    if nombre==datos.get("cines").get("cinesaparquesur").get("nombre"):
        lista.append(datos.get("cines").get("cinesaparquesur").get("direccion"))
        lista.append(datos.get("cines").get("cinesaparquesur").get("encuentra"))
    if nombre==datos.get("cines").get("cinesaprincipepio").get("nombre"):
        lista.append(datos.get("cines").get("cinesaprincipepio").get("direccion"))
        lista.append(datos.get("cines").get("cinesaprincipepio").get("encuentra"))
    if nombre==datos.get("cines").get("yelmoalcorcon").get("nombre"):
        lista.append(datos.get("cines").get("yelmoalcorcon").get("direccion"))
        lista.append(datos.get("cines").get("yelmoalcorcon").get("encuentra"))
    return lista

def info (datos,sesion):
    lista=[]
    if sesion in datos.get("cines").get("cinecallao").get("sesiones"):
        lista.append(datos.get("cines").get("cinecallao").get("nombre"))
    if sesion in datos.get("cines").get("cinesaprincipepio").get("sesiones"):
        lista.append(datos.get("cines").get("cinesaprincipepio").get("nombre"))
    if sesion in datos.get("cines").get("cinesaparquesur").get("sesiones"):
        lista.append(datos.get("cines").get("cinesaparquesur").get("nombre"))
    if sesion in datos.get("cines").get("yelmoalcorcon").get("sesiones"):
        lista.append(datos.get("cines").get("yelmoalcorcon").get("nombre"))
    return lista

def libre (datos,horas):
    lista=[]
    if horas==datos.get("sesiones").get("cinco").get("hora"):
        lista.append(datos.get("sesiones").get("cinco").get("pelicula"))   
    if horas==datos.get("sesiones").get("cuatro").get("hora"):
        lista.append(datos.get("sesiones").get("cuatro").get("pelicula"))
    if horas==datos.get("sesiones").get("tres").get("hora"):
        lista.append(datos.get("sesiones").get("tres").get("pelicula"))
    if horas==datos.get("sesiones").get("dos").get("hora"):
        lista.append(datos.get("sesiones").get("dos").get("pelicula"))
    if horas==datos.get("sesiones").get("uno").get("hora"):
        lista.append(datos.get("sesiones").get("uno").get("pelicula"))
    if horas==datos.get("sesiones").get("seis").get("hora"):
        lista.append(datos.get("sesiones").get("seis").get("pelicula"))
    if horas==datos.get("sesiones").get("siete").get("hora"):
        lista.append(datos.get("sesiones").get("siete").get("pelicula"))
    return lista


