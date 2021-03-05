from lxml import etree

def listar (datos):
    nombre=datos.xpath("/tv/channel/@id")
    return nombre