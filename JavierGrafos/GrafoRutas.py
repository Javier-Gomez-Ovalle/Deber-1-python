from NodosAristas import Nodo, Arista

# clase para manejar el grafo de rutas
class GrafoRutas:
    def __init__(self):
        # diccionario para guardar todos los nodos
        # clave = nombre de la ciudad
        # valor = objeto Nodo
        self.nodos = {}
    
    def obtener_o_crear_nodo(self, nombre_ciudad):
        # si el nodo ya existe, lo devuelve
        # si no existe, lo crea y lo agrega al diccionario
        if nombre_ciudad not in self.nodos:
            nuevo_nodo = Nodo(nombre_ciudad)
            self.nodos[nombre_ciudad] = nuevo_nodo
        return self.nodos[nombre_ciudad]
    
    def agregar_conexion(self, ciudad_origen, ciudad_destino):
        # obtener o crear los nodos
        nodo_origen = self.obtener_o_crear_nodo(ciudad_origen)
        nodo_destino = self.obtener_o_crear_nodo(ciudad_destino)
        
        # crear la arista (conexion)
        nueva_arista = Arista(nodo_origen, nodo_destino)
        
        # agregar la arista al nodo de origen
        nodo_origen.agregar_conexion(nueva_arista)
        
        print(f"Conexión agregada: {ciudad_origen} -> {ciudad_destino}")
    
    def mostrar_grafo(self):
        # recorrer todos los nodos
        for nombre_ciudad, nodo in self.nodos.items():
            print(f"\nNodo: {nombre_ciudad}")
            
            # mostrar las conexiones de este nodo
            if nodo.conexiones:
                for arista in nodo.conexiones:
                    print(f"  → {arista.destino.nombre}")
            else:
                print("  (sin conexiones salientes)")