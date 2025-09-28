#creamos las torres y le pasamos los parametros a la primera
primera = [3, 2, 1]  
segunda = []         
tercera = []         

discos = len(primera)
movimientos_total = (2 ** discos) - 1

#movimiento entre 2 torres
def hacer_movimiento(torre1, torre2, nombre1, nombre2):
    if len(torre1) == 0:
        disco = torre2.pop()
        torre1.append(disco)
        print(f"Movemos el disco {disco} de {nombre2} a {nombre1}")
    elif len(torre2) == 0:
        disco = torre1.pop()
        torre2.append(disco)
        print(f"Movemos el disco {disco} de {nombre1} a {nombre2}")
    elif torre1[-1] < torre2[-1]:
        disco = torre1.pop()
        torre2.append(disco)
        print(f"Movemos el disco {disco} de {nombre1} a {nombre2}")
    else:
        disco = torre2.pop()
        torre1.append(disco)
        print(f"Movemos el disco {disco} de {nombre2} a {nombre1}")

#aqui resolvemos las torres de hanoi
for i in range(movimientos_total):
    if discos % 2 == 1:
        #ciclo para los discos impares
        if i % 3 == 0:
            hacer_movimiento(primera, tercera, "Primera", "Tercera")
        elif i % 3 == 1:
            hacer_movimiento(primera, segunda, "Primera", "Segunda")
        else:
            hacer_movimiento(segunda, tercera, "Segunda", "Tercera")
    else:
        #ciclo para los discos pares
        if i % 3 == 0:
            hacer_movimiento(primera, segunda, "Primera", "Segunda")
        elif i % 3 == 1:
            hacer_movimiento(primera, tercera, "Primera", "Tercera")
        else:
            hacer_movimiento(segunda, tercera, "Segunda", "Tercera")

print("Primera torre:", primera)
print("Segunda torre:", segunda) 
print("Tercera torre:", tercera)