from GrafoRutas import GrafoRutas
from GenerarMapa import GeneradorMapa
def main():
    print("CALCULADOR DE RUTAS CON GRAFOS")
    
    #le pedimos al usuario que ponga un origen
    origen = input("Ingrese la ciudad de origen: ").strip()
    
    #le pedimos al usuario que ponga un destino
    destino = input("Ingrese la ciudad de destino: ").strip()
    
    #le pedimos al usuario que introduzca paradas intermedias
    print("\nIngrese las paradas intermedias, separelas por comas... Ej: 'Bogota, Ibague, Medellin'")
    paradas_input = input("Paradas: ").strip()
    
    #convertimos las paradas en una lista
    if paradas_input:
        #separamos los datos por comas y quitamos los espacios
        paradas = [p.strip() for p in paradas_input.split(",")]
    else:
        paradas = []
    
    print("\n--- Procesando ruta ---")
    print(f"Origen: {origen}")
    print(f"Destino: {destino}")
    print(f"Paradas: {paradas}")
    
    #creamos el grafo de rutas
    grafo = GrafoRutas()
    
    # construir la ruta completa en orden
    # la ruta va: origen -> parada1 -> parada2 -> ... -> destino
    ruta_completa = [origen] + paradas + [destino]
    
    # agregar cada tramo al grafo
    for i in range(len(ruta_completa) - 1):
        ciudad_actual = ruta_completa[i]
        ciudad_siguiente = ruta_completa[i + 1]
        grafo.agregar_conexion(ciudad_actual, ciudad_siguiente)
    
    # mostrar el grafo
    print("\n--- Estructura del Grafo ---")
    grafo.mostrar_grafo()
    
    # generar el mapa con la ruta
    print("\n--- Generando mapa ---")
    generador = GeneradorMapa()
    url_mapa = generador.crear_mapa(ruta_completa)
    
    print("\n=== RUTA GENERADA ===")
    print(f"Abra este enlace en su navegador:")
    print(url_mapa)
    print("\nEl mapa mostrará la mejor ruta entre estos puntos.")

# ejecutar el programa
if __name__ == "__main__":
    main()