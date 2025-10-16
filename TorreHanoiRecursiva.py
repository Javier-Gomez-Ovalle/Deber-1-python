Primera = [3, 2, 1]  
Segunda = []         
Tercera = []

def mover_torres(numero_discos, origen, destino, aux):
    if numero_discos == 1:
        destino.append(origen.pop())
        print(f"Mover disco a {destino}")
    else:
        mover_torres(numero_discos-1, origen, aux, destino)
        destino.append(origen.pop())
        print(f"Mover disco a {destino}")
        mover_torres(numero_discos-1, aux, destino, origen)

mover_torres(3, Primera, Tercera, Segunda)
print("Primera torre:", Primera)
print("Segunda torre:", Segunda)
print("Tercera torre:", Tercera)