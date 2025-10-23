class BusquedaBinaria:
    
    #creamos una funcion recursiva para la busqueda binaria
    def buscar(self, lista, objetivo, izq=0, der=None):
        #si es la primera llamada, definir derecha
        if der is None:
            der = len(lista) - 1
        #creamos nuestro caso base que sera, si la izquierda pasa a la derecha entonces este no existe
        #calculamos posicion del medio
        medio = (izq+ der) // 2
        #cuando se cumple el  caso base nos dice que si lo encontramos
        if lista[medio] == objetivo:
            return True
        
        #creamos el caso recursivo: buscar en mitad derecha
        elif lista[medio] < objetivo:
            return self.buscar(lista, objetivo, medio + 1, der)
        
        #segundo caso recursivo: buscar en mitad izquierda
        else:
            return self.buscar(lista, objetivo, izq, medio - 1)