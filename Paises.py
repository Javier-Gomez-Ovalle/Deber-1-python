import requests

#funcion para conectarse a la api
def obtener_datos():
    url = "https://restcountries.com/v3.1/region/europe"
    respuesta = requests.get(url)
    data = respuesta.json()
    return data

#traer informacion de todos los paises
data_paises = obtener_datos()

#sacar solo los nombres de los paises
lista_paises = []
for pais in data_paises:
    lista_paises.append(pais["name"]["common"])

# ordenar para poder usar busqueda binaria
lista_paises.sort()

# preguntar al usuario que pais buscar
pais_buscar = input("Ingrese el nombre del pais: ")

#busqueda lineal
def busqueda_lineal(pais):
    for elemento in data_paises:
        if elemento["name"]["common"] == pais:
            return elemento["maps"]["googleMaps"]
    return "No encontrado"

#busqueda binaria
def busqueda_binaria(lista, pais):
    inicio = 0
    final = len(lista) - 1
    
    while inicio <= final:
        medio = (inicio + final) // 2
        if lista[medio] == pais:
            for info in data_paises:
                if info["name"]["common"] == pais:
                    return info["maps"]["googleMaps"]
        elif lista[medio] < pais:
            inicio = medio + 1
        else:
            final = medio - 1
    return "No encontrado"

resultado_lineal = busqueda_lineal(pais_buscar)
resultado_binario = busqueda_binaria(lista_paises, pais_buscar)

print("Resultado busqueda lineal:", resultado_lineal)
print("Resultado busqueda binaria:", resultado_binario)