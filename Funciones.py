import json 
with open ("archivojson.json") as fichero:
    datos=json.load(fichero)

def listar (datos):
    lista=[]
    for i in datos["cines"]:
        lista.append(i)
    return lista

