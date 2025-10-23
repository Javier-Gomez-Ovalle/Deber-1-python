from api_pokemon import ConsumirAPI
from grafo_evolucion import GrafoEvolucion
from buscar_pokemon import BusquedaBinaria

def main():
    url_api = "https://pokeapi.co/api/v2/evolution-chain/1/"
    
    print("obteniendo datos de la api")

    api = ConsumirAPI(url_api)
    datos = api.obtener_datos()
    

    if datos is None:
        print("Error: No se pudo obtener la informacion")
        return
    print("\nConstruyendo grafo de evoluciones...")
    grafo = GrafoEvolucion()
    grafo.construir_grafo(datos["chain"])
    
    print("\nGrafo de evoluciones:")
    grafo.mostrar_grafo()
    
    lista_nombres = sorted(grafo.nodos.keys())
    print("\nLista ordenada de pokemones:", lista_nombres)
    

    buscador = BusquedaBinaria()
    
    pokemon1 = "ivysaur"
    print(f"\nBuscando '{pokemon1}'...")
    encontrado1 = buscador.buscar(lista_nombres, pokemon1)
    if encontrado1:
        print(f"✓ {pokemon1} SI esta en la cadena")
    else:
        print(f"✗ {pokemon1} NO esta en la cadena")
    
    pokemon2 = "charmander"
    print(f"\nBuscando '{pokemon2}'...")
    encontrado2 = buscador.buscar(lista_nombres, pokemon2)
    if encontrado2:
        print(f"✓ {pokemon2} SI esta en la cadena")
    else:
        print(f"✗ {pokemon2} NO esta en la cadena")

if __name__ == "__main__":
    main()