class GrafoEvolucion:
    def __init__(self):
        # creamos el diccionario para guardar los nodos
        # asignamos que la clave sea el nombre del pokemon
        # hacemops que el valor sea la  lista de pokemones a los que evoluciona
        self.nodos={}
    
    # funcion recursiva para construir el grafo
    def construir_grafo(self,cadena):
        # sacar el nombre del pokemon actual
        nombre_actual = cadena["species"]["name"]
        
        # sacamos los nombres de las evoluciones
        evoluciones= []
        for evolucion in cadena["evolves_to"]:
            nombre_evo = evolucion["species"]["name"]
            evoluciones.append(nombre_evo)
        
        #agregamos al grafo
        self.nodos[nombre_actual] = evoluciones
        
        #llamamos recursivamente para cada evolucion
        for evolucion in cadena["evolves_to"]:
            self.construir_grafo(evolucion)
    
    # creamos la funcion para mostrar el grafo
    def mostrar_grafo(self):
        for pokemon, evoluciones in self.nodos.items():
            if evoluciones:
                print(f"{pokemon} -> {evoluciones}")
            else:
                print(f"{pokemon} -> []")