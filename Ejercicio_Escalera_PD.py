def contar_formas_escalera(n, memo=None):
    if memo is None:
        memo = {}
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = (contar_formas_escalera(n-1, memo) + contar_formas_escalera(n-2, memo) +contar_formas_escalera(n-3, memo))
    return memo[n]

nEscalones = int(input("Cuantos escalones quiere subir?: "))
print("Cantidad de formas de subir la esos escalones:", contar_formas_escalera(nEscalones))
