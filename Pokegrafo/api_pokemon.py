import requests

#creamos la clase para consumir la api de pokemon
class ConsumirAPI:
    def __init__(self, url):
        self.url=url
    
    #creamos una funcion para obtener los datos
    def obtener_datos(self):
        try:
            #hacemos la peticion a la api
            respuesta = requests.get(self.url,timeout=10)
            #verificamos si hubo error http
            respuesta.raise_for_status()
            
        except requests.exceptions.Timeout:
            # except por si tarda mucho en responder
            print("error: la api tardo mucho en responder")
            return None
            
        except requests.exceptions.ConnectionError:
            #verificamos si no se cuenta con internet o la url no existe
            print("error: no se pudo conectar a la api")
            return None
            
        except requests.exceptions.HTTPError as e:
            # except para cuando la api devuelve error 200 300 400 o 500
            print(f"error http {e}")
            return None
            
        except requests.exceptions.RequestException as e:
            #cualquier otro error de requests
            print(f"error en la peticion: {e}")
            return None
        
        try:
            #convertimos la respuesta a json
            datos_json=respuesta.json()
            return datos_json
            
        except ValueError:
            # si la respuesta no es json valido
            print("error: la respuesta no es un json valido")
            return None