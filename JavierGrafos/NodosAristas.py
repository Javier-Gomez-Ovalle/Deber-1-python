#en esta clase representamos los nodos que seran las ciudades
class Nodo:
    def __init__(self,nombre):
        #le asignamos un nombre a la ciudad
        self.nombre=nombre
        #creamos una lista en la que guardaremos las conexiones, osea, las aristas
        self.conexiones=[]
    
    def agregar_conexion(self, arista):
        #agrergamos una arista a este nodo
        self.conexiones.append(arista)

#creamos una clase para representar las aristas, osea, la conexion entre nodos
class Arista:
    def __init__(self, origen, destino):
        #ubicamos el nodo desde donde sale la ruta
        self.origen = origen
        #ubiacmos el nodo hacia donde llega la ruta
        self.destino =destino