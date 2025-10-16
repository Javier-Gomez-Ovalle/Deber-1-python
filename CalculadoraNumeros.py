def sumar_digitos(num):
    if num < 10:
        return num
    else:
        ult_digito = num % 10
        restante = num // 10
        return ult_digito + sumar_digitos(restante)

numero_ingresado = int(input("Ingrese un numero: "))
resultado = sumar_digitos(numero_ingresado)
print("la suma de los numeros es:", resultado)