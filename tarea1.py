import random

def barajar_mazo():
    palos = ["c", "t", "d", "p"]
    valores = list(range(1, 14))
    mazo=[]
    
    for palo in palos:
        for valor in valores:
            mazo.append((valor,palo))
    
    random.shuffle(mazo)
    return mazo

def insertion_sort(lista):
    n = len(lista)
    
    for i in range(1, n):
        key = lista[i]
        j = i - 1
        
        while j >= 0 and key< lista[j]:
            lista[j + 1]= lista[j]
            j -= 1
        lista[j + 1]= key
    return lista

mazo = barajar_mazo()
print(f"Mazo original: {mazo}")

mazo_ordenado= insertion_sort(mazo)
print(f"Mazo ordenado: {mazo_ordenado}")