def calcular_total(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

numeros = [10.0, 25.0, 15.0]
resultado = calcular_total(numeros)
print(f"Total dos números: {resultado}")