import webbrowser

# clase para generar el mapa de google maps
class GeneradorMapa:
    
    def crear_mapa(self, ruta_ciudades):
        # ruta_ciudades es una lista con todas las ciudades en orden
        # ejemplo: ["Ibague", "Honda", "Barranquilla"]
        
        if len(ruta_ciudades) < 2:
            print("Error: Se necesitan al menos 2 ciudades")
            return None
        
        # separar origen y destino
        origen = ruta_ciudades[0]
        destino = ruta_ciudades[-1]
        
        # las paradas intermedias (waypoints) son las ciudades del medio
        paradas = ruta_ciudades[1:-1]
        
        # construir la url de google maps
        url_base = "https://www.google.com/maps/dir/?api=1"
        
        # agregar origen
        url = f"{url_base}&origin={origen}"
        
        # agregar destino
        url += f"&destination={destino}"
        
        # agregar paradas si existen
        if paradas:
            # unir las paradas con "|" como pide google maps
            waypoints = "|".join(paradas)
            url += f"&waypoints={waypoints}"
        
        # modo de transporte (driving = conduciendo)
        url += "&travelmode=driving"
        
        return url
    
    def abrir_en_navegador(self, url):
        # abre automaticamente el mapa en el navegador
        try:
            webbrowser.open(url)
            print("Mapa abierto en el navegador")
        except:
            print("No se pudo abrir el navegador automaticamente")