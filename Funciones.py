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